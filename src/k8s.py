import time
import copy
import yaml
from kubernetes import config, client

TIMEOUT_LIMIT = 120.0


class K8sApi:

    def __init__(self):
        config.load_incluster_config()
        self.namespace = "default"
        self.port = 2137
        self.core_api = client.CoreV1Api()
        self.apps_api = client.AppsV1Api()
        self.batch_api = client.BatchV1Api()
        self.lobby_ip = self._get_lobby_ip()
        with open("game-server.yaml", "r") as whatever:
            self.game_server = yaml.load(whatever, yaml.SafeLoader)
        with open("inside-job.yaml", "r") as whatever:
            self.job = yaml.load(whatever, yaml.SafeLoader)

    def _get_lobby_ip(self):
        try:
            self.list_pods()
        except Exception as error:
            with open("log.info", "a") as log_file:
                log_file.write(f"{error}")
        for item in pod_list:
            try:
                if item.metadata.labels["app"] == "lobby":
                    return item.status.host_ip
            except Exception as error:
                with open("log.info", "a") as log_file:
                    log_file.write(f"{error}")
        return None

    def create_game_server(self):
        server = copy.deepcopy(self.game_server)
        server["metadata"]["name"] += f"-{port}"
        args:str = server["spec"]["containers"][0]["args"][0]
        args.replace("port", f"{self.port}")
        self.port += 1
        try:
            self.apps_api.create_namespaced_deployment(self.namespace, server)
            return True
        except Exception as error:
            with open("log.info", "a") as log_file:
                log_file.write(f"{error}")
            return False
    
    def list_game_servers(self):
        try:
            self.list_pods()
        except Exception as error:
            with open("log.info", "a") as log_file:
                log_file.write(f"{error}")
            return list()
        servers = []
        for item in pod_list:
            try:
                if item.spec.template.metada.labels["app"] == "game-server":
                    address = item.status.host_ip + ":" + \
                        item.metadata.name[-4:]
                    servers.append(address)
            except Exception as error:
                with open("log.info", "a") as log_file:
                    log_file.write(f"{error}")
        return servers

    def list_pods(self):
        pods = self.core_api.list_namespaced_pod("default").items
        return pods

    def run_code_and_get_results(self, question_id: str, code_object: dict):
        results = dict()
        for user, answer in code_object.items():
            results[user] = None
            inside_job = copy.deepcopy(self.job)
            inside_job["metadata"]["name"] = user
            task = \
                answer + f" ; python3 /root/devxdev/tests/test{question_id}.py"
            inside_job["spec"]["containers"][0]["args"][0] = task
        try:
            self.batch_api.create_namespaced_job(self.namespace, inside_job)
        except Exception as error:
            with open("log.info", "a") as log_file:
                log_file.write(f"{error}")
            return results
        time.sleep(TIMEOUT_LIMIT)
        try:
            job_list = self.batch_api.list_namespaced_job(self.namespace).items
            for item in job_list:
                if item.metadata.name in results.keys():
                    if item.status.succeeded >= 1:
                        results[item.metadata.name] = True
                    else:
                        results[item.metadata.name] = False
            return results
        except Exception as error:
            with open("log.info", "a") as log_file:
                log_file.write(f"{error}")
            return results


if __name__ == "__main__":
    k8s = K8sApi()
    k8s.print_pods()
