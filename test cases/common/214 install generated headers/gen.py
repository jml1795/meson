#!/usr/bin/env python3

import os, argparse, json

parser = argparse.ArgumentParser()
parser.add_argument('--outdir', required=True)
parser.add_argument('ifiles', nargs='+')

options = parser.parse_args()
outdir = options.outdir
ifiles = options.ifiles

for i, ifile_name in enumerate(ifiles):
    with open(ifile_name) as f:
        data = json.load(f)

        nm = data["name"]
        hdr = '#pragma once\nstruct {} {{\n'.format(nm)
        impl = '#include "{}.hpp"\n'.format(nm)
        for mem in data["members"]:
            hdr += '   {} m_{} = {{}};\n'.format(mem["type"], mem["name"])
            hdr += '   {} {}() const;\n'.format(mem["type"], mem["name"])
            impl += '{} {}::{}() const {{ return m_{}; }}\n'.format(mem["type"], nm, mem["name"], mem["name"])

        hdr += '};'
        stem = os.path.splitext(os.path.basename(ifile_name))[0]
        with open(os.path.join(outdir, stem + '.hpp'), 'w+') as hpp:
            hpp.write(hdr)
        with open(os.path.join(outdir, stem + '.cpp'), 'w+') as cpp:
            cpp.write(impl)
