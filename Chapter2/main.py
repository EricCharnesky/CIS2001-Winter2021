from ball import Ball


def juggle(ball1, ball2, ball3):
    ball1.catch()
    ball2.catch()
    ball3.toss()

    ball1.toss()
    ball3.catch()

    ball2.toss()
    ball1.catch()


basketball = Ball("Basketball")
basketball.toss()
baseball = Ball("Baseball")
baseball.toss()
raquetball = Ball("Raquetball")
raquetball.toss()

juggle(basketball, baseball, raquetball)

print(basketball)
print(baseball)
print(raquetball)

# don't access "private" values directly
# basketball._is_moving = True
