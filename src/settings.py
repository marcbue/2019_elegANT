class ControllerParams:

    def __init__(self, framerate=30):
        super(ControllerParams, self).__init__()
        self.framerate = framerate
        self.create_ant_time = 2


class ModelParams:

    def __init__(self):
        super(ModelParams, self).__init__()


class ViewParams:

    def __init__(self):
        super(ViewParams, self).__init__()


class AllParams:

    def __init__(self, controller_params, model_params, view_params):
        self.controller_params: ControllerParams = controller_params
        self.model_params: ModelParams = model_params
        self.view_params: ViewParams = view_params


c_p = ControllerParams()
m_p = ModelParams()
v_p = ViewParams()

all_params = AllParams(controller_params=c_p,
                       model_params=m_p,
                       view_params=v_p
                       )
