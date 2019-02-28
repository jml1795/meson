project('simple', 'cpp', 'cuda', version : '1.0.0')

# subdir('shared')

cxx = meson.get_compiler('cpp')
magick_dep = dependency('MagickCore') # pulls in openmp
cudart_dep = declare_dependency(dependencies: [meson.get_compiler('cpp').find_library('cudart', required: true)])
exe = shared_library('lib', 'lib.cpp', 'kernels.cu', dependencies: [magick_dep, cudart_dep])
