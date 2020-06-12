import time
import copy
import yaml
from kubernetes import config, client
import constant

TIMEOUT_LIMIT = 120.0


class K8sApi:

    def __init__(self):
        config.load_incluster_config()
        self.namespace = "default"
        self.nodeport = 32137
        self.core_api = client.CoreV1Api()
        self.apps_api = client.AppsV1Api()
        self.batch_api = client.BatchV1Api()
        self.lobby_ip = constant.LOBBY_URL
        with open("/opt/devxdev/src/game-server.yaml", "r") as whatever:
            self.game_server = yaml.load(whatever, yaml.SafeLoader)
        with open("/opt/devxdev/src/inside-job.yaml", "r") as whatever:
            self.job = yaml.load(whatever, yaml.SafeLoader)
        with open("/opt/devxdev/src/game-server-service.yaml", "r") as whatever:
            self.game_server_service = yaml.load(whatever, yaml.SafeLoader)

    def create_game_server(self):
        server = copy.deepcopy(self.game_server)
        service = copy.deepcopy(self.game_server_service)

        server["spec"]["template"]["metadata"]["labels"]["port"] = str(self.nodeport)
        server["metadata"]["name"] += f"-{self.nodeport}"
        server["spec"]["template"]["metadata"]["labels"]["app"] += f"-{self.nodeport}"
        server["spec"]["selector"]["matchLabels"]["app"] += f"-{self.nodeport}"

        service["metadata"]["name"] += f"-{self.nodeport}"
        service["spec"]["selector"]["app"] += f"-{self.nodeport}"
        service["spec"]["ports"][0]["port"] = self.nodeport
        service["spec"]["ports"][0]["nodePort"] = self.nodeport
        self.nodeport += 1
        try:
            self.apps_api.create_namespaced_deployment(self.namespace, server)
            self.core_api.create_namespaced_service(self.namespace, service)
            time.sleep(10)
            return True
        except Exception as error:
            print(f"{error}")
            return False

    def list_game_servers(self):
        try:
            pod_list = self.list_pods()
        except Exception as error:
            print(f"{error}")
            return list()
        servers = []
        for item in pod_list:
            try:
                if "game-server" in item.metadata.labels["app"]:
                    address = "http://" + constant.LOBBY_DOMAIN_NAME + ":" + \
                        item.metadata.labels["port"]
                    servers.append(address)
            except Exception as error:
                print(f"{error}")
        return servers

    def list_pods(self):
        pods = self.core_api.list_namespaced_pod("default").items
        return pods

    def run_code_and_get_results(self, question_id: str, code_object: dict):
        print("got here too")
        results = dict()
        for user, answer in code_object.items():
            print(user, answer)
            results[user] = False
            inside_job = copy.deepcopy(self.job)
            inside_job["metadata"]["name"] = user
            task = \
                answer + f"\npython3 /opt/devxdev/tasks/test{question_id}.py"
            inside_job["spec"]["template"]["spec"]["containers"][0]["args"][0] = task
            print(task)
        try:
            self.batch_api.create_namespaced_job(self.namespace, inside_job)
        except Exception as error:
            print(f"{error}")
            return results
        print("started")
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
            print(f"{error}")
            return results
