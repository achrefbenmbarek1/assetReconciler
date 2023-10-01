# from reconciliationStrategyChooser.entity.ReconciliationStrategy import ReconciliationStrategy
# from reconciliationStrategyChooser.infrastructure.repository.ReconciliationStrategyRepositoryImp import ReconciliationStrategyRepositoryImp
# from reconciliationStrategyChooser.interactor.CreateStrategyHandler import CreateStrategyHandler
# from shared.eventInfrastructure.eventBus.MessageBroker import MessageBroker



# tableauAmortissement = pd.read_excel('inventory.xlsx',sheet_name = "ta")
# tableauInventaire = pd.read_excel('inventory.xlsx', sheet_name="inv")
# print(tableauInventaire)
# print(tableauAmortissement)
#
#
# indexer = recordlinkage.Index()
# indexer.block(left_on = 'NumFiche', right_on = 'NumFiche')
# candidates = indexer.index(tableauAmortissement, tableauInventaire)
# print("this is candidates")
# print(candidates)
#
#
# compare = recordlinkage.Compare()
# compare.string('NumFiche','NumFiche',method ='jarowinkler',label = "numFicheScore")
# compare.string('Intitule','Intitule',method ='jarowinkler',label = "intituleScore")
# features = compare.compute(candidates,tableauAmortissement, tableauInventaire)
# potentialMatches = features[features.sum(axis = 1) > 1].reset_index()
# potentialMatches['Score'] = potentialMatches.loc[:,'numFicheScore':'intituleScore'].sum(axis = 1)
# print(potentialMatches)
# potential_match_1 = tableauAmortissement.loc[1]
# potential_match_2 = tableauInventaire.loc[0]
# print("this is potential one")
# print(potential_match_1)
# print("this is potential 2")
# print(potential_match_2)
# for index, row in tableauAmortissement.iterrows():
#     print(row)
# curiosity = tableauAmortissement.isin([ 'Siege', 'pwc' ])
# print(curiosity.any().any())
# for row in tableauAmortissement.itertuples():
#     print(tableauAmortissement[tableauAmortissement['Etablissement'] == 'Siege'])




excelFile = "inventory.xlsx"
# eventStore:EventStoreMongoDbImp = EventStoreMongoDbImp(dbName="eventstore", collectionName="events") 
# eventBus:EventBus = EventBus(eventStore)
# reconciliationStrategy:CyclicAutomaticReconcilation = CyclicAutomaticReconcilation()
# eventBus.subscribe("NonPreviouslyReconsiledInvAndTaWereFilteredByQuantity",reconciliationStrategy)
if __name__ == "__main__":
    # broker = MessageBroker()
    # reconciliationStrategyRepository = ReconciliationStrategyRepositoryImp("mongodb","mongodb://localhost:27017/","Strategies")
    # createStrategy = CreateStrategyHandler(reconciliationStrategyRepository, broker)
    
    
    
