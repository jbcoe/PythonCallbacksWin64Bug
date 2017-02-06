#!/usr/bin/env python

import argparse
import sys
import os
import subprocess
import platform

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
default_build_dir = os.path.join(script_dir, '../build')

def _build_parser():
    parser = argparse.ArgumentParser(
            description='Runs CMake with platform-appropriate arguments')

    parser.add_argument(
        '-p',
        '--prepare',
        help='prepare a build with cmake',
        dest='prepare',
        action='store_true')

    parser.add_argument(
        '-t',
        '--tests',
        help='run all tests with cmake',
        dest='tests',
        action='store_true')

    parser.add_argument(
        '-o',
        '--output',
        help='path for cmake build',
        dest='output_path',
        default=default_build_dir)

    parser.add_argument(
        '-c',
        '--configuration',
        help='build configuration',
        dest='build_config',
        default='Debug')

    parser.add_argument(
        '--python-path',
        help='path to python executable ie "/usr/local/bin/python3"',
        dest='python_path')

    if platform.system() == 'Windows':
        parser.add_argument(
            '--win32',
            help='Build 32-bit libraries',
            action='store_true',
            dest='win32')

    return parser.parse_args()


def _get_cmake_invocation(args):
    if platform.system() == 'Windows':
        invocation = ['cmake', root_dir, '-B{}'.format(args.output_path)]
        if args.win32:
            invocation.extend(['-G', 'Visual Studio 14 2015'])
        else:
            invocation.extend(['-G', 'Visual Studio 14 2015 Win64'])
    else:
        invocation = ['cmake', root_dir, '-G', 'Ninja']
        invocation.append('-DCMAKE_BUILD_TYPE={}'.format(args.build_config))
    
    if args.python_path:
        invocation.append('-DPYTHON_EXECUTABLE={}'.format(args.python_path))
    
    return invocation


def _get_build_invocation(args):
    invocation = ['cmake', '--build', args.output_path]
    return invocation


def main():
    args = _build_parser()

    args.output_path = os.path.abspath(args.output_path)
    # VS puts intermediate files in config-specific subdirs for us
    if platform.system() == 'Windows':
        pass
    else:
        args.output_path = os.path.join(args.output_path, args.build_config)

    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    subprocess.check_call(_get_cmake_invocation(args), cwd=args.output_path)
    subprocess.check_call(_get_build_invocation(args), cwd=root_dir)

    rc = 0
    if args.tests:
        rc = subprocess.call(['ctest', '-C', args.build_config, '--output-on-failure'], cwd=args.output_path)

    # For CI builds we want a fail return status if tests fail; test failure prevents installer creation.
    if rc != 0:
        sys.exit(-1)

if __name__ == "__main__":
    main()

