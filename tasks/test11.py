# Create txt file named "SpacesToUnderlines" containing the words 

# "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
# Vivamus volutpat cursus odio, sed molestie nulla tincidunt eu. 
# Quisque in sem elit. Maecenas scelerisque augue eu purus sodales dapibus. 
# Phasellus sodales, massa vel convallis mollis, metus ante eleifend libero, eleifend porta erat tortor non augue. 
# Aliquam quis feugiat magna. Quisque non purus sed nisl pellentesque rutrum. Vivamus pellentesque et sem eu pretium. 
# Suspendisse egestas tristique tincidunt. Pellentesque purus felis, tincidunt a mollis id, imperdiet eu risus. Morbi vitae tellus est. 
# Phasellus maximus lorem varius tortor egestas finibus vitae a justo. Mauris sit amet pretium erat. Vivamus ac dui a ante venenatis posuere eu sed lacus. 
# Maecenas vulputate metus sed gravida condimentum.".

# Change all spaces to underlines.

import os

def main():

    assert os.path.isfile(os.path.expanduser('~/SpacesToUnderlines.txt'))
    f = open("~/SpacesToUnderlines.txt", "r")
    assert(f.read() == "Lorem_ipsum_dolor_sit_amet,_consectetur_adipiscing_elit._Vivamus_volutpat_cursus_odio,_sed_molestie_nulla_tincidunt_eu._Quisque_in_sem_elit._Maecenas_scelerisque_augue_eu_purus_sodales_dapibus._Phasellus_sodales,_massa_vel_convallis_mollis,_metus_ante_eleifend_libero,_eleifend_porta_erat_tortor_non_augue._Aliquam_quis_feugiat_magna._Quisque_non_purus_sed_nisl_pellentesque_rutrum._Vivamus_pellentesque_et_sem_eu_pretium._Suspendisse_egestas_tristique_tincidunt._Pellentesque_purus_felis,_tincidunt_a_mollis_id,_imperdiet_eu_risus._Morbi_vitae_tellus_est._Phasellus_maximus_lorem_varius_tortor_egestas_finibus_vitae_a_justo._Mauris_sit_amet_pretium_erat._Vivamus_ac_dui_a_ante_venenatis_posuere_eu_sed_lacus._Maecenas_vulputate_metus_sed_gravida_condimentum.")

if __name__== "__main__":
       main()