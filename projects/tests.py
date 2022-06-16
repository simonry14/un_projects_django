from django.test import TestCase
from .models import project, country, theme, approval_status, donor, fund, lead_org_unit

# Create your tests here.

class ProjectTestCase(TestCase):
    def testProject(self):
        _project = project(project_title="Title", country=country(), theme=theme(), approval_status=approval_status(), donor=donor(), 
                          lead_org_unit=lead_org_unit(), fund=fund(), start_date="StartDate", end_date="EndDate")
        self.assertEqual(_project.project_title, "Title")
        #self.assertEqual(_project.country, country())
        #self.assertEqual(_project.theme, theme())
        #self.assertEqual(_project.approval_status, approval_status())
        #self.assertEqual(_project.lead_org_unit, lead_org_unit())
        #self.assertEqual(_project.fund, fund())
        self.assertEqual(_project.start_date, "StartDate")
        self.assertEqual(_project.end_date, "EndDate")
        #self.assertEqual(_project.donor, donor())
