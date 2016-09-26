evaluationTime = 300

popSize = 50

NUM_ENVIRONMENTS = 4

NUM_GENERATIONS = 500



SCALING_FACTOR = 0.1

OBSTACLE_HEIGHT = 0.5 * SCALING_FACTOR

OBSTACLE_WIDTH = 2.0 * SCALING_FACTOR

OBSTACLE_LENGTH = 1.0 * SCALING_FACTOR

BARRIER_LENGTH = 8.0

LIGHT_SOURCE_HEIGHT = OBSTACLE_HEIGHT / 10.0


NUM_ROBOT_PARTS = 7

ROBOT_HEIGHT = 0.25 * SCALING_FACTOR

ROBOT_WIDTH = 0.5 * SCALING_FACTOR

ROBOT_LENGTH = 0.75 * SCALING_FACTOR

WHEEL_RADIUS = ROBOT_HEIGHT/2.0

WHEEL_SPEED = 20.0

MAX_ACCELERATION = 0.1


NUM_SENSORS = 4

NUM_HIDDEN_NEURONS = 6

NUM_MOTORS = 2

MAX_HIDDEN_TAU = 0.3

IDENTITY_TRANSFER_FUNCTION = 0

TANH_TRANSFER_FUNCTION = 1



TOTAL_BINARY_BASES = 560

BASES_PER_THREAD = 80

MAX_THREADS = int( TOTAL_BINARY_BASES / BASES_PER_THREAD )

MAX_WIRES_PER_THREAD = 4

NUM_PARAMETERS_PER_WIRE = 5 # x,y,direction,distance,weight

PIN_ROWS = NUM_SENSORS + NUM_HIDDEN_NEURONS + NUM_MOTORS

PIN_COLUMNS = 10

UP         = 0
UP_RIGHT   = 1
RIGHT      = 2
DOWN_RIGHT = 3
DOWN       = 4
DOWN_LEFT  = 5
LEFT       = 6
UP_LEFT    = 7

