import gravitysim


def main():
    space = gravitysim.sim.GravitySpace(g=0.01, fps=60, strict=False)
    circle = gravitysim.sim.Circle(
        pos=(830, 600),
        speed=(0, -8),
        acc=(0, 0),
        mass=15,
        rad=50,
        clr=gravitysim.colors.white
    )

    circle2 = gravitysim.sim.Circle(
        pos=(1100, 600),
        speed=(0, 0),
        acc=(0, 0),
        mass=13,
        rad=50,
        clr=gravitysim.colors.green
    )

    space.add_object(circle)
    space.add_object(circle2)
    space.center(circle2)

    space.start()


if __name__ == '__main__':
    main()
