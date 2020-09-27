from pipeline_manager import pipeline


def test_pipeline_manager():
    add_step = pipeline()
    a = []

    @add_step
    def step1():
        a.append(1)

    @add_step(depends_on=["step1"])
    def step2():
        a.append(2)

    @add_step(depends_on=["step1", "step2"])
    def step3():
        a.append(3)

    @add_step(depends_on=["step1", "step2", "step3"])
    def step4():
        a.append(4)

    step4()
    assert a == [1, 1, 2, 1, 1, 2, 3, 4]

    a = []
    step3()
    assert a == [1, 1, 2, 3]

    @add_step
    def step5():
        a.append(5)

    a = []
    step4()
    assert a == [1, 1, 2, 1, 1, 2, 3, 4]

    a = []
    step5()
    assert a == [5]
