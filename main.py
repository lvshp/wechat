import werobot

robot = werobot.WeRoBot(token='lvspfacai')

@robot.handler
def hello(message):
    return 'hello world'

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8088