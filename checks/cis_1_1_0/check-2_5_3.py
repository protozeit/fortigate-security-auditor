from checker import Checker

class Check_CIS_2_5_3(Checker):

    def __init__(self, firewall, display, verbose=False):
        
        super().__init__(firewall, display, verbose)
        
        self.id = "2.5.3"
        self.title = "Ensure HA Reserved Management Interface is Configured"
        self.levels = [1, 2]
        self.auto = True
        self.benchmark_version = "v1.1.0"
        self.benchmark_author = "CIS"

    def do_check(self):
        self.add_message('Not implemented')
        return None