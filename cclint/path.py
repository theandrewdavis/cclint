# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Olli Wang. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#    * Neither the name of Olli Wang nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os

import cpplint


def expand_directory(dirname, filenames=None, recursive=False,
                     excludedirs=None):
    """Searches files with matched extensions within a directory.

    Args:
        dirname: The directory to search for.
        filenames: The list of filenames to return. This variable is used when
            using this function as a recursive function. This function enters
            recursive mode when the `recursive` parameter is `True`.
        recursive: Whether to search files within subdirectories recursively.
        excludedirs: A list of directories to exclude from searching.

    Returns:
        A list of matched filenames.
    """
    if excludedirs is not None and dirname in excludedirs:
        return list()

    if filenames is None:
        filenames = list()

    for item in os.listdir(dirname):
        filename = os.path.join(dirname, item)

        if os.path.isdir(filename):
            if recursive:
                expand_directory(filename, filenames, True, excludedirs)
        elif os.path.isfile(filename) and \
           os.path.splitext(item)[1][1:] in cpplint._valid_extensions:
            filenames.append(filename)

    return filenames
