class email_logit(logit):
    '''
    一个logit的现实版本,可以在函数调用时发送email给管理员
    '''
    def __init__(self, email = 'admin@myproject.com', *arg, **kwargs):
        self.email =email
        super(email_logit, self). __init__(*arg, **kwargs)
        
    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass