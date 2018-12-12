from .BaseService import BaseService
from ..DTO import VisitDTO, EmployeeDTO, CheckpointDTO, EventVisitDTO, CameraDTO, DepartmentDTO
from ...DAL import EntitiesUnit, Employee, Checkpoint, Camera, Department, Visit


class StatisticsSearchResult:

    def __init__(self, first_name, last_name, address, event, date_time):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.event = event
        self.date_time = date_time


class StatisticsService(BaseService):

    def search_visits(self, department_name='---', first_name='', last_name='', ckpt_address='---', event='---', considering_time=False, start_date=None, stop_date=None):

        employee_search_params = []
        ckpt_search_params = []
        visit_search_params = []

        if department_name != '---':
            dept = self._db.department_repository.find([Department.name == department_name])
            if dept:
                employee_search_params.append(Employee.dept_id == dept[0].id)
            else:
                return None, 0

        if first_name:
            employee_search_params.append(Employee.first_name == first_name)
        if last_name:
            employee_search_params.append(Employee.last_name == last_name)

        if ckpt_address != '---':
            ckpt = self._db.checkpoint_repository.find([Checkpoint.address == ckpt_address])
            if ckpt:
                ckpt_search_params.append(Camera.id == ckpt[0].id)
            else:
                return None, 0

        if event != '---':
            events = list([i.value for i in EventVisitDTO])
            event_ind = events.index(event)
            visit_search_params.append(Visit.event == events[event_ind])

        if not visit_search_params:
            visits = self._db.visit_repository.get_all()
        else:
            visits = self._db.visit_repository.find(visit_search_params)

        if considering_time:
            to_delete = []
            for v in visits:
                if not start_date<=v.datetime.date()<=stop_date:
                    to_delete.append(v)
            [visits.remove(v) for v in to_delete]

        result = []

        if employee_search_params:
            found_employees = self._db.employee_repository.find(employee_search_params)
            found_employees_id = [empl.id for empl in found_employees]
            if found_employees_id:
                for v in visits:
                    if v.emp_id in found_employees_id:
                        result.append(v)
        if ckpt_search_params:
            found_cameras = self._db.camera_repository.find(ckpt_search_params)
            found_cameras_id = [cam.id for cam in found_cameras]
            if found_cameras_id:
                for v in visits:
                    if v.camera_id in found_cameras_id:
                        if v not in result:
                            result.append(v)

        if not result and not employee_search_params and not ckpt_search_params:
            result = visits

        self._searched_visits = self._convert_visits_to_results(result)
        return self._searched_visits, len(self._searched_visits) if self._searched_visits else 0

    def get_all_visits(self):
        visits = self._db.visit_repository.get_all()
        self._searched_visits = self._convert_visits_to_results(visits)
        return self._searched_visits, len(self._searched_visits) if self._searched_visits else 0

    def _convert_visits_to_results(self, visits):
        results = []
        for visit in visits:
            empl = self._db.employee_repository.find([Employee.id == visit.emp_id])[0]
            cam = self._db.camera_repository.find([Camera.id == visit.camera_id])[0]
            ckpt = self._db.checkpoint_repository.find([Checkpoint.id == cam.ckpt_id])[0]
            res = StatisticsSearchResult(empl.first_name, empl.last_name, ckpt.address, visit.event, visit.datetime)
            results.append(res)
        self._searched_visits = results
        return results

    def get_chief(self, department_name='---'):
        if department_name != '---' and department_name:
            dept = self._db.department_repository.find([Department.name == department_name])
            emp = self._db.employee_repository.find([Employee.dept_id == dept[0].id])
            if emp:
                emp = emp[0]
                return f'{emp.first_name} {emp.last_name}'
        return ''

    def get_departments(self):
        depts_name = ['---']
        depts = self._db.department_repository.get_all()
        [depts_name.append(d.name) for d in depts]
        return depts_name

    def get_checkpoints(self):
        ckpts_address = ['---']
        ckpts = self._db.checkpoint_repository.get_all()
        [ckpts_address.append(ckpt.address) for ckpt in ckpts]
        return ckpts_address

    def save_statistics(self, path):
        pass

    def __init__(self, connection_string):
        super().__init__()
        self._searched_visits = []
        self._db = EntitiesUnit(connection_string)
