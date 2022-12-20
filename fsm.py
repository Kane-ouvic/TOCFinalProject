from transitions.extensions import GraphMachine
class Model:

    def clear_state(self, deep=False, force=False):
        print("Clearing state ...")
        return True

    def test_state(self, deep=False, force=False):
        print("Testing state ...")
        return True
    
    def enter_init_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_init_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_echo_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_echo_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_choice_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_choice_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_exchange_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_exchange_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_invoice_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_invoice_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_invoice_start_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_invoice_start_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_invoice_compare_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_invoice_compare_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_invoice_finish_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_invoice_finish_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_todo_list_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_todo_list_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_todo_create_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_todo_create_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_todo_date_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_todo_date_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_todo_progress_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_todo_progress_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_todo_progress_update_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_todo_progress_update_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_todo_status_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_todo_status_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_todo_status_update_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_todo_status_update_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_weather_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_weather_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_foodmap_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def exit_foodmap_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_show_fsm_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True
    
    def enter_outer_website_state(self, deep=False, force=False):
        print("Enter init state ...")
        return True

    def go_back(self, deep=False, force=False):
        print("go_back ...")
        return True
    


model = Model()
machine = GraphMachine(model=model, states=['init', 'echo', 'choice', 'exchange','foodmap','invoice','invoice-start','invoice-compare','invoice-finish',
                                            'todo-list','todo-create','todo-date','todo-progress-update','todo-progress','todo-status-update','todo-status','weather','show-fsm', 'outer-website'],
                       transitions=[
                           {'trigger': 'send-message', 'source': 'init', 'dest': 'show-fsm',
                            'conditions': model.enter_show_fsm_state},
                           {'trigger': 'reply', 'source': 'show-fsm', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'send-message', 'source': 'init', 'dest': 'weather',
                            'conditions': model.enter_weather_state},
                           {'trigger': 'reply', 'source': 'weather', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'send-message', 'source': 'init', 'dest': 'echo',
                            'conditions': model.enter_echo_state},
                           {'trigger': 'reply', 'source': 'echo', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'send-message', 'source': 'init', 'dest': 'foodmap',
                            'conditions': model.enter_foodmap_state},
                           {'trigger': 'reply', 'source': 'foodmap', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'send-message', 'source': 'init', 'dest': 'exchange',
                            'conditions': model.enter_exchange_state},
                           {'trigger': 'reply', 'source': 'exchange', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'send-message', 'source': 'init', 'dest': 'choice',
                            'conditions': model.enter_choice_state},
                           {'trigger': 'reply', 'source': 'choice', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'send-message', 'source': 'init', 'dest': 'invoice',
                            'conditions': model.enter_init_state},
                           {'trigger': 'reply', 'source': 'invoice', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'click-button', 'source': 'invoice', 'dest': 'invoice-start',
                            'conditions': model.enter_invoice_start_state},
                           {'trigger': 'click-button', 'source': 'invoice-start', 'dest': 'invoice-compare',
                            'conditions': model.enter_invoice_compare_state},
                           {'trigger': 'reply', 'source': 'invoice-compare', 'dest': 'invoice-finish',
                            'conditions': model.enter_invoice_finish_state},
                           {'trigger': 'click-button', 'source': 'invoice-finish', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'reply', 'source': 'init', 'dest': 'todo-list',
                            'conditions': model.enter_todo_list_state},
                           {'trigger': 'reply', 'source': 'init', 'dest': 'todo-create',
                            'conditions': model.enter_todo_create_state},
                           {'trigger': 'reply', 'source': 'todo-create', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'click-button', 'source': 'todo-list', 'dest': 'todo-status',
                            'conditions': model.enter_todo_status_state},
                           {'trigger': 'reply', 'source': 'todo-status', 'dest': 'todo-status-update',
                            'conditions': model.enter_todo_status_update_state},
                           {'trigger': 'click-button', 'source': 'todo-list', 'dest': 'todo-progress',
                            'conditions': model.enter_todo_progress_state},
                           {'trigger': 'reply', 'source': 'todo-progress', 'dest': 'todo-progress-update',
                            'conditions': model.enter_todo_progress_update_state},
                           {'trigger': 'click-button', 'source': 'todo-list', 'dest': 'todo-date',
                            'conditions': model.enter_todo_date_state},
                           {'trigger': 'reply', 'source': 'todo-progress-update', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'reply', 'source': 'todo-status-update', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'reply', 'source': 'todo-date', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'click-button', 'source': 'foodmap', 'dest': 'outer-website',
                            'conditions': model.enter_outer_website_state},
                           {'trigger': 'reply', 'source': 'outer-website', 'dest': 'init',
                            'conditions': model.go_back},
                           {'trigger': 'send-message', 'source': 'invoice-compare', 'dest': 'invoice-compare',
                            'conditions': model.enter_invoice_compare_state},
                           {'trigger': 'click-button', 'source': 'choice', 'dest': 'choice',
                            'conditions': model.enter_choice_state}
],
    initial='init', show_conditions=True)

model.get_graph().draw('fsm.png', prog='dot')
