mamba_sample
============

python mamba sample repository

# Usage

<pre>
usage: mamba [-h] [--version] [--slow SLOW] [--enable-coverage]
             [--format {documentation,progress}] [--no-color] [--watch]
             [specs [specs ...]]

positional arguments:
  specs                 Specs or directories with specs to run (default:
                        ['spec', 'specs'])

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         Display the version.
  --slow SLOW, -s SLOW  Slow test threshold in seconds (default: 0.075)
  --enable-coverage     Enable code coverage measurement (default: False)
  --format {documentation,progress}, -f {documentation,progress}
                        Output format (default: documentation)
  --no-color            Turn off all output coloring (default: False)
  --watch, -w           Enable file watching support - not available with
                        python3 (default: False)
</pre>

* --documentation
test result is shown like normal documentation style
https://github.com/nestorsalceda/mamba/blob/master/mamba/formatters.py#L40

* --progress
test result is shown like "..*F..."
https://github.com/nestorsalceda/mamba/blob/master/mamba/formatters.py#L161

# References

* https://github.com/nestorsalceda/mamba
* http://nestorsalceda.github.io/mamba/
