project('simple', 'cpp', 'cuda', version : '1.0.0')

subdir('shared')

cxx = meson.get_compiler('cpp')
cudart_dep = declare_dependency(dependencies: [cxx.find_library('cudart', required: true)])
thread_dep = dependency('threads')
magick_dep = dependency('MagickCore') # pulls in openmp
exe = shared_library('lib', 'lib.cpp', dependencies: [libkernels, thread_dep, magick_dep, cudart_dep])
