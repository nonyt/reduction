from recipes.almahelpers import fixsyscaltimes # SACM/JAO - Fixes
__rethrow_casa_exceptions = True
context = h_init()
context.set_state('ProjectSummary', 'proposal_code', '2017.1.01355.L')
context.set_state('ProjectSummary', 'piname', 'unknown')
context.set_state('ProjectSummary', 'proposal_title', 'unknown')
context.set_state('ProjectStructure', 'ous_part_id', 'X327499494')
context.set_state('ProjectStructure', 'ous_title', 'Undefined')
context.set_state('ProjectStructure', 'ppr_file', '/opt/dared/opt/qa56.1712.1/mnt/dataproc/2017.1.01355.L_2018_07_16T20_35_16.444/SOUS_uid___A001_X1296_X155/GOUS_uid___A001_X1296_X156/MOUS_uid___A001_X1296_X15d/working/PPR_uid___A001_X1296_X15e.xml')
context.set_state('ProjectStructure', 'ps_entity_id', 'uid://A001/X1220/Xddd')
context.set_state('ProjectStructure', 'recipe_name', 'hsd_calimage')
context.set_state('ProjectStructure', 'ous_entity_id', 'uid://A001/X1220/Xdd9')
context.set_state('ProjectStructure', 'ousstatus_entity_id', 'uid://A001/X1296/X15d')
try:
    hsd_importdata(vis=['uid___A002_Xc99ad7_Xab4a', 'uid___A002_Xcc8b19_X7112', 'uid___A002_Xcc8b19_X7d16', 'uid___A002_Xcf3a9c_X1be5', 'uid___A002_Xcf7c14_X14ca'], session=['session_1', 'session_2', 'session_2', 'session_4', 'session_5'])
    hsd_flagdata(pipelinemode="automatic")
    h_tsyscal(pipelinemode="automatic")
    hsd_tsysflag(pipelinemode="automatic")
    hsd_skycal(pipelinemode="automatic")
    hsd_k2jycal(pipelinemode="automatic")
    hsd_applycal(pipelinemode="automatic")
    hsd_baseline(pipelinemode="automatic")
    hsd_blflag(pipelinemode="automatic")
    hsd_baseline(pipelinemode="automatic")
    hsd_blflag(pipelinemode="automatic")
    hsd_imaging(pipelinemode="automatic")
finally:
    h_save()
