project('install_generated_headers', 'cpp',
  version : '1.0.0',
  default_options : ['warning_level=3',
                     'cpp_std=c++14'])

gen_prgm = find_program( join_paths(meson.current_source_dir(), 'gen.py'), required: true )

gen = generator(
  gen_prgm, output: ['@BASENAME@.hpp', '@BASENAME@.cpp'],
  arguments : ['--outdir=@BUILD_DIR@', '@INPUT@'],
)

src = files('test.json')

generated_src = gen.process(src)

exe = shared_library(
  'install_generated_headers', generated_src,
  install : true
)

install_headers(generated_src)
