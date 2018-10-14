from BiometricACS.DAL import *
from BiometricACS.BLL.DTO.AccountDTO import AccountDTO
from BiometricACS.BLL.DTO.EnumsDTO import AccountRoleDTO
from BiometricACS.BLL.Infrastructure.ServiceModule import connection_string
from BiometricACS.BLL.Services import AuthorizationService
from BiometricACS.APP import program_settings
from BiometricACS.APP.Subsystems.ProgramLogging import Log
import pickle


role = 'technical_engineer'
print(list([i.value for i in AccountRoleDTO]).index(role))
print(list(AccountRoleDTO)[list([i.value for i in AccountRoleDTO]).index(role)])

# a = 5
# print(len(a))

# print(Log.get_visit_log(True, 'Denis', 'Kolpakov'))

# db = EntitiesUnit(connection_string)
# print(db.account_repository.get_all())


# service = AuthorizationService()
#
# acc = AccountDTO('delprosha', '123364')
# result, acc = service.is_registred(acc)
# print(acc)


# db = EntitiesUnit(connection_string=connection_string)
#
# print(db.account_repository.get_all())
# a = AccountDTO('delprosha', '123364', AccountRoleDTO.viewer)
# a.id = 9
# # print(a)
# # a = db.account_repository.find(Account.username==a.username)[0]
# db.account_repository.update(a)
# # db.save()
# db.save()

# new_acc = db.account_repository.find(Account.username == a.username)[0]
# new_acc.username = 'delprosha'
# db.account_repository.delete(new_acc)
# db.save()
