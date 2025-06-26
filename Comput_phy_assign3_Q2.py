import numpy as np
import matplotlib.pyplot as plt

# Initial Conditions
G = 6.673 * 10**-11  # Gravitational constant
Ms = 1.0e30          # Mass of the Sun
Me = 6 * 10**24      # Mass of Earth
Mj = 100*1.898e27        # Mass of Jupiter
r_es = 1.5e11        # Earth-Sun distance
r_js = 7e11          # Jupiter-Sun distance
r_ej = 6.3e11        # Earth-Jupiter distance
num_steps = 365      # Simulate for 1 year
dt = 60 * 60 * 24    # A day in seconds

# Initial velocities
vxe = 0.0
vxj = 0.0
v_ey = np.sqrt(G * Ms / r_es)  # Earth's orbital velocity
vyj = np.sqrt(G * Ms / r_js)  # Jupiter's orbital velocity


# Initial positions
x_e, y_e = 1.496e11, 0
x_j, y_j = 7e11, 0
x_s, y_s = 0, 0

# Sun's velocity to ensure center of mass is fixed
v_sx = 0.0
v_sy = -(Me * v_ey + Mj * vyj) / Ms

# Lists to store positions
earthx = []
Jupiterx = []
earthy = []
Jupitery = []
Sunx = []
Suny = []

# Gravitational force function
def gravitational_force(m, x2, x1, y2, y1):
    r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    a = -G * m * (x2 - x1) / r**3
    return a

# Simulation loop
for n in range(20*num_steps):
    # For Earth
    vxe_next = vxe + ((gravitational_force(Ms, x_e, x_s, y_e, y_s) + gravitational_force(Mj, x_e, x_j, y_e, y_j)) * dt)
    x_e_next = x_e + (vxe_next * dt)
    vye_next = v_ey + ((gravitational_force(Ms, y_e, y_s, x_e, x_s) + gravitational_force(Mj, y_e, y_j, x_e, x_j)) * dt)
    y_e_next = y_e + (vye_next * dt)

    earthx.append(x_e)
    earthy.append(y_e)

    vxe = vxe_next
    x_e = x_e_next
    v_ey = vye_next
    y_e = y_e_next

    # For Jupiter
    vxj = vxj + ((gravitational_force(Ms, x_j, x_s, y_j, y_s) + gravitational_force(Me, x_j, x_e, y_j, y_e)) * dt)
    x_j = x_j + (vxj * dt)
    vyj = vyj + ((gravitational_force(Ms, y_j, y_s, x_j, x_s) + gravitational_force(Me, y_j, y_e, x_j, x_e)) * dt)
    y_j = y_j + (vyj * dt)

    Jupiterx.append(x_j)
    Jupitery.append(y_j)

    # For Sun
    v_sx = v_sx + ((gravitational_force(Mj, x_s, x_j, y_s, y_j) + gravitational_force(Me, x_s, x_e, y_s, y_e)) * dt)
    x_s = x_s + (v_sx * dt)
    v_sy = v_sy + ((gravitational_force(Mj, y_s, y_j, x_s, x_j) + gravitational_force(Me, y_s, y_e, x_s, x_e)) * dt)
    y_s = y_s + (v_sy * dt)

    Sunx.append(x_s)
    Suny.append(y_s)

# Plotting
plt.plot(Jupiterx, Jupitery, label="Jupiter")
plt.plot(earthx, earthy, label="Earth")
plt.plot(Sunx, Suny, label="Sun")
plt.xlabel('x (m)')
plt.ylabel('y (m)')
#plt.xlim(-.25e13,.25e13)
#plt.ylim(-.25e13,.25e13)
plt.legend()
plt.title('Orbits of Earth and Jupiter')
plt.show()