import numpy as np

# Criação de Arrays
arr = np.array([1, 2, 3])
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
full = np.full((2, 3), 7)
eye = np.eye(3)
identity = np.identity(3)
empty = np.empty((2, 2))
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)
logspace = np.logspace(0, 2, 5)
meshgrid = np.meshgrid(np.arange(0, 5), np.arange(0, 5))
diag = np.diag([1, 2, 3])
tri = np.tri(3)
function_from = np.fromfunction(lambda i, j: i + j, (3, 3))
iter_from = np.fromiter([1, 2, 3], dtype=int)
buffer_from = np.frombuffer(b'Hello', dtype='S1')



# Manipulação de Arrays
reshaped = np.reshape(arr, (3, 1))
raveled = arr.ravel()
flattened = arr.flatten()
transposed = arr.T
swapped_axes = np.swapaxes(arr, 0, 1)
moved_axis = np.moveaxis(arr, 0, 1)
expanded = np.expand_dims(arr, axis=0)
squeezed = np.squeeze(arr)
concatenated = np.concatenate([arr, arr])
stacked = np.stack([arr, arr])
hstacked = np.hstack([arr, arr])
vstacked = np.vstack([arr, arr])
dstacked = np.dstack([arr, arr])
column_stacked = np.column_stack([arr, arr])
row_stacked = np.row_stack([arr, arr])
splitted = np.split(arr, 2)
hsplitted = np.hsplit(arr, 2)
vsplitted = np.vsplit(arr, 2)
dsplitted = np.dsplit(arr, 2)
tiled = np.tile(arr, 3)
repeated = np.repeat(arr, 2)


# Indexação e Slicing
taken = np.take(arr, [1, 2])
put = np.put(arr, [1, 2], [10, 20])
chosen = np.choose([0, 1, 2], [arr, arr, arr])
diagonal = np.diagonal(arr)
selected = np.select([arr > 2, arr < 5], [arr * 2, arr / 2])
compressed = np.compress(arr > 2, arr)
extracted = np.extract(arr > 2, arr)
where = np.where(arr > 2)
nonzero = np.nonzero(arr)
argwhere = np.argwhere(arr > 2)
argmax = np.argmax(arr)
argmin = np.argmin(arr)
argsort = np.argsort(arr)
argpartition = np.argpartition(arr, 2)


# Estatísticas e Agregação
sum_arr = np.sum(arr)
mean_arr = np.mean(arr)
median_arr = np.median(arr)
std_arr = np.std(arr)
var_arr = np.var(arr)
min_arr = np.min(arr)
max_arr = np.max(arr)
ptp_arr = np.ptp(arr)
percentile_arr = np.percentile(arr, 50)
quantile_arr = np.quantile(arr, 0.5)
corrcoef = np.corrcoef(arr, arr)
cov = np.cov(arr, arr)


# Operações Matemáticas
add = np.add(arr, 1)
subtract = np.subtract(arr, 1)
multiply = np.multiply(arr, 2)
divide = np.divide(arr, 2)
floor_divide = np.floor_divide(arr, 2)
mod = np.mod(arr, 2)
power = np.power(arr, 2)
reciprocal = np.reciprocal(arr)
negative = np.negative(arr)
absolute = np.abs(arr)
fabs = np.fabs(arr)
sign = np.sign(arr)
clip = np.clip(arr, 0, 5)
round_arr = np.round(arr, 2)
ceil = np.ceil(arr)
floor = np.floor(arr)
trunc = np.trunc(arr)
exp = np.exp(arr)
expm1 = np.expm1(arr)
log = np.log(arr)
log10 = np.log10(arr)
log2 = np.log2(arr)
log1p = np.log1p(arr)
sqrt = np.sqrt(arr)
cbrt = np.cbrt(arr)
square = np.square(arr)

# Funções Trigonométricas
sin_arr = np.sin(arr)
cos_arr = np.cos(arr)
tan_arr = np.tan(arr)
arcsin_arr = np.arcsin(arr)
arccos_arr = np.arccos(arr)
arctan_arr = np.arctan(arr)
arctan2_arr = np.arctan2(arr, arr)
deg2rad = np.deg2rad(arr)
rad2deg = np.rad2deg(arr)
hypot = np.hypot(arr, arr)
sinh = np.sinh(arr)
cosh = np.cosh(arr)
tanh = np.tanh(arr)
arcsinh = np.arcsinh(arr)
arccosh = np.arccosh(arr)
arctanh = np.arctanh(arr)


# Comparação e Lógica
greater = np.greater(arr, 2)
greater_equal = np.greater_equal(arr, 2)
less = np.less(arr, 2)
less_equal = np.less_equal(arr, 2)
equal = np.equal(arr, 2)
not_equal = np.not_equal(arr, 2)
logical_and = np.logical_and(arr > 2, arr < 5)
logical_or = np.logical_or(arr > 2, arr < 5)
logical_xor = np.logical_xor(arr > 2, arr < 5)
logical_not = np.logical_not(arr > 2)
isfinite = np.isfinite(arr)
isinf = np.isinf(arr)
isnan = np.isnan(arr)
isneginf = np.isneginf(arr)
isposinf = np.isposinf(arr)


# Álgebra Linear
inv = np.linalg.inv(arr)
det = np.linalg.det(arr)
norm = np.linalg.norm(arr)
solve = np.linalg.solve(arr, arr)
eig = np.linalg.eig(arr)
eigh = np.linalg.eigh(arr)
qr = np.linalg.qr(arr)
svd = np.linalg.svd(arr)
pinv = np.linalg.pinv(arr)
cholesky = np.linalg.cholesky(arr)
rank = np.linalg.matrix_rank(arr)
cond = np.linalg.cond(arr)
eigvals = np.linalg.eigvals(arr)

"""
# Geradores Aleatórios
rand = np.random.rand(3, 2)
randn = np.random.randn(3, 2)
randint = np.random.randint(0, 10, size=(3, 2))
uniform = np.random.uniform(0, 1, size=(3, 2))
normal = np.random.normal(0, 1, size=(3, 2))
choice = np.random.choice([1, 2, 3], size=5)
permutation = np.random.permutation(10)
shuffle = np.random.shuffle(arr)
beta = np.random.beta(1, 1, size=(3, 2))
gamma = np.random.gamma(2, 2, size=(3, 2))
exponential = np.random.exponential(1, size=(3, 2))
poisson = np.random.poisson(5, size=(3, 2))
binomial = np.random.binomial(10, 0.5, size=(3, 2))
geometric = np.random.geometric(0.5, size=(3, 2))
lognormal = np.random.lognormal(0, 1, size=(3, 2))
multinomial = np.random.multinomial(10, [0.2, 0.3, 0.5], size=3)
seed = np.random.seed(0)
"""

# Transformadas e Espectro
fft = np.fft.fft(arr)
ifft = np.fft.ifft(arr)
fft2 = np.fft.fft2(arr)
ifft2 = np.fft.ifft2(arr)
fftshift = np.fft.fftshift(arr)
ifftshift = np.fft.ifftshift(arr)
rfft = np.fft.rfft(arr)
irfft = np.fft.irfft(arr)


# Operações em Arrays Booleanos
any = np.any(arr)
all = np.all(arr)
count_nonzero = np.count_nonzero(arr)


# Operações com Tipos de Dados
dtype = np.dtype('float32')
astype = arr.astype('float32')
itemsize = arr.itemsize
byteswap = arr.byteswap()
copy = arr.copy()


# Entrada e Saída de Dados
loadtxt = np.loadtxt('file.txt')
savetxt = np.savetxt('file.txt', arr)
load = np.load('file.npy')
save = np.save('file.npy', arr)
savez = np.savez('file.npz', arr)
savez_compressed = np.savez_compressed('file.npz', arr)
fromfile = np.fromfile('file.bin', dtype='float32')
tofile = np.tofile('file.bin', arr)


# Outras Funções Úteis
unique = np.unique(arr)
sort = np.sort(arr)
partition = np.partition(arr, 2)
bincount = np.bincount(arr)
histogram = np.histogram(arr, bins=10)
digitize = np.digitize(arr, bins=[1, 2, 3])
cumsum = np.cumsum(arr)
cumprod = np.cumprod(arr)
diff = np.diff(arr)
ediff1d = np.ediff1d(arr)
gradient = np.gradient(arr)
meshgrid = np.meshgrid(arr, arr)
mgrid = np.mgrid[0:3, 0:3]
ogrid = np.ogrid[0:3, 0:3]
