# from ..sound.echo import echo_test # from game.sound.echo import echo_sound
#
# def render_test():
#     print("render")
#     echo_test()


# from game.sound.echo import echo_test # 책에 있는 import문인데 나랑 경로가 달라서 실행이 안됨 아래와 같이 수정
# from JumpToPython.game.sound.echo import echo_test


# from game.sound.echo import echo_test
# 이 파일을 직접실행하면 모듈이 없다고 뜨는데
# 파이썬 인터프리터로 from game.graphic.render import render_test 를 입력하면 잘 실행된다.

# 아래가 바로 relative 접근
# 단 입력은 꼭 모듈안에서만 입력해야함
# 인터프리터에서 하면 오류!
from ..sound.echo import echo_test # 얘도 인터프리터에서 from game.graphic.render import render_test 하면 잘 실행됨

def render_test():
    print("render") #
    echo_test() #
