
#!/usr/bin/env python
"""
"""
from fabric.api import run, execute, task
from fabric.api import env, hosts, roles, run


env.abort_exception = None
"""
Fabric normally handles aborting by printing an error message to stderr and calling sys.exit(1). This setting allows you to override that behavior (which is what happens when env.abort_exception is None.)

Give it a callable which takes a string (the error message that would have been printed) and returns an exception instance. That exception object is then raised instead of SystemExit (which is what sys.exit does.)

Much of the time you'll want to simply set this to an exception class, as those fit the above description perfectly (callable, take a string, return an exception instance.) E.g. env.abort_exception = MyExceptionClass.
"""


env.abort_on_prompts = False
"""
When True, Fabric will run in a non-interactive mode, calling abort anytime it would normally prompt the user for input (such as password prompts, "What host to connect to?" prompts, fabfile invocation of prompt, and so forth.) This allows users to ensure a Fabric session will always terminate cleanly instead of blocking on user input forever when unforeseen circumstances arise.

New in version 1.1.

See also
--abort-on-prompts
"""


env.all_hosts = None
"""
Default: None

Set by fab to the full host list for the currently executing command. For informational purposes only.

See also
Execution model
"""


env.always_use_pty = True
"""
Default: True

When set to False, causes run/sudo to act as if they have been called with pty=False.

See also
--no-pty

New in version 1.0.
"""


env.colorize_errors = False
"""
Default False

When set to True, error output to the terminal is colored red and warnings are colored magenta to make them easier to see.

New in version 1.7.
"""


env.combine_stderr = True
"""
Default: True

Causes the SSH layer to merge a remote program's stdout and stderr streams to avoid becoming meshed together when printed. See Combining stdout and stderr for details on why this is needed and what its effects are.

New in version 1.0.
"""


env.command = None
"""
Default: None

Set by fab to the currently executing command name (e.g., when executed as $ fab task1 task2, env.command will be set to "task1" while task1 is executing, and then to "task2".) For informational purposes only.

See also
Execution model
"""


env.command_prefixes = []
"""
Default: []

Modified by prefix, and prepended to commands executed by run/sudo.

New in version 1.0.
"""


env.command_timeout = None
"""
Default: None

Remote command timeout, in seconds.

New in version 1.6.

See also
--command-timeout
"""


env.connection_attempts = 1
"""
Default: 1

Number of times Fabric will attempt to connect when connecting to a new server. For backwards compatibility reasons, it defaults to only one connection attempt.

New in version 1.4.

See also
--connection-attempts, timeout
"""


env.cwd = ''
"""
Default: ''

Current working directory. Used to keep state for the cd context manager.
"""


env.dedupe_hosts = True
"""
Default: True

Deduplicate merged host lists so any given host string is only represented once (e.g. when using combinations of @hosts + @roles, or -H and -R.)

When set to False, this option relaxes the deduplication, allowing users who explicitly want to run a task multiple times on the same host (say, in parallel, though it works fine serially too) to do so.

New in version 1.5.
"""


env.disable_known_hosts = False
"""
Default: False

If True, the SSH layer will skip loading the user's known-hosts file. Useful for avoiding exceptions in situations where a "known host" changing its host key is actually valid (e.g. cloud servers such as EC2.)

See also
--disable-known-hosts, SSH behavior
"""


env.eagerly_disconnect = False
"""
Default: False

If True, causes fab to close connections after each individual task execution, instead of at the end of the run. This helps prevent a lot of typically-unused network sessions from piling up and causing problems with limits on per-process open files, or network hardware.

Note
When active, this setting will result in the disconnect messages appearing throughout your output, instead of at the end. This may be improved in future releases.
"""


env.exclude_hosts = []
"""
Default: []

Specifies a list of host strings to be skipped over during fab execution. Typically set via --exclude-hosts/-x.

New in version 1.1.
"""


env.fabfile = 'fabfile.py'
"""
Default: fabfile.py

Filename pattern which fab searches for when loading fabfiles. To indicate a specific file, use the full path to the file. Obviously, it doesn't make sense to set this in a fabfile, but it may be specified in a .fabricrc file or on the command line.

See also
--fabfile, fab options and arguments
"""


env.gateway = None
"""
Default: None

Enables SSH-driven gatewaying through the indicated host. The value should be a normal Fabric host string as used in e.g. env.host_string. When this is set, newly created connections will be set to route their SSH traffic through the remote SSH daemon to the final destination.

New in version 1.5.

See also
--gateway
"""


env.host_string = None
"""
Default: None

Defines the current user/host/port which Fabric will connect to when executing run, put and so forth. This is set by fab when iterating over a previously set host list, and may also be manually set when using Fabric as a library.

See also
Execution model
"""


env.forward_agent = False
"""
Default: False

If True, enables forwarding of your local SSH agent to the remote end.

New in version 1.4.

See also
--forward-agent
"""


env.host = None
"""
Default: None

Set to the hostname part of env.host_string by fab. For informational purposes only.
"""


env.hosts = []
"""
Default: []

The global host list used when composing per-task host lists.

See also
--hosts, Execution model
"""


env.keepalive = 0
"""
Default: 0 (i.e. no keepalive)

An integer specifying an SSH keepalive interval to use; basically maps to the SSH config option ClientAliveInterval. Useful if you find connections are timing out due to meddlesome network hardware or what have you.

See also
--keepalive

New in version 1.1.
"""


env.key = None
"""
Default: None

A string, or file-like object, containing an SSH key; used during connection authentication.

Note
The most common method for using SSH keys is to set key_filename.

New in version 1.7.
"""


env.key_filename = None
"""
Default: None

May be a string or list of strings, referencing file paths to SSH key files to try when connecting. Passed through directly to the SSH layer. May be set/appended to with -i.

See also
Paramiko's documentation for SSHClient.connect()
"""


env.linewise = False
"""
Default: False

Forces buffering by line instead of by character/byte, typically when running in parallel mode. May be activated via --linewise. This option is implied by env.parallel - even if linewise is False, if parallel is True then linewise behavior will occur.

See also
Linewise vs bytewise output

New in version 1.3.
"""


#env.local_user
"""
A read-only value containing the local system username. This is the same value as user's initial value, but whereas user may be altered by CLI arguments, Python code or specific host strings, local_user will always contain the same value.
"""


env.no_agent = False
"""
Default: False

If True, will tell the SSH layer not to seek out running SSH agents when using key-based authentication.

New in version 0.9.1.

See also
--no_agent
"""


env.no_keys = False
"""
Default: False

If True, will tell the SSH layer not to load any private key files from one's $HOME/.ssh/ folder. (Key files explicitly loaded via fab -i will still be used, of course.)

New in version 0.9.1.

See also
-k
"""


env.parallel = False
"""
Default: False

When True, forces all tasks to run in parallel. Implies env.linewise.

New in version 1.3.

See also
--parallel, Parallel execution
"""


env.password = None
"""
Default: None

The default password used by the SSH layer when connecting to remote hosts, and/or when answering sudo prompts.

See also
--initial-password-prompt, env.passwords, Password management
"""


env.passwords = {}
"""
Default: {}

This dictionary is largely for internal use, and is filled automatically as a per-host-string password cache. Keys are full host strings and values are passwords (strings).

See also
Password management

New in version 1.0.
"""


env.path = ''
"""
Default: ''

Used to set the $PATH shell environment variable when executing commands in run/sudo/local. It is recommended to use the path context manager for managing this value instead of setting it directly.

New in version 1.0.
"""


env.pool_size = 0
"""
Default: 0

Sets the number of concurrent processes to use when executing tasks in parallel.

New in version 1.3.

See also
--pool-size, Parallel execution
"""


env.port = None
"""
Default: None

Set to the port part of env.host_string by fab when iterating over a host list. May also be used to specify a default port.
"""


env.real_fabfile = None
"""
Default: None

Set by fab with the path to the fabfile it has loaded up, if it got that far. For informational purposes only.

See also
fab options and arguments
"""


env.remote_interrupt = None
"""
Default: None

Controls whether Ctrl-C triggers an interrupt remotely or is captured locally, as follows:

None (the default): only open_shell will exhibit remote interrupt behavior, and run/sudo will capture interrupts locally.
False: even open_shell captures locally.
True: all functions will send the interrupt to the remote end.
New in version 1.6.
"""


env.rcfile = '$HOME/.fabricrc'
"""
Default: $HOME/.fabricrc

Path used when loading Fabric's local settings file.

See also
--config, fab options and arguments
"""


env.reject_unknown_hosts = False
"""
Default: False

If True, the SSH layer will raise an exception when connecting to hosts not listed in the user's known-hosts file.

See also
--reject-unknown-hosts, SSH behavior
"""


env.system_known_hosts = None
"""
Default: None

If set, should be the path to a known_hosts file. The SSH layer will read this file before reading the user's known-hosts file.

See also
SSH behavior
"""


env.roledefs = {}
"""
Default: {}

Dictionary defining role name to host list mappings.

See also
Execution model
"""


env.roles = []
"""
Default: []

The global role list used when composing per-task host lists.

See also
--roles, Execution model
"""


env.shell = '/bin/bash -l -c'
"""
Default: /bin/bash -l -c

Value used as shell wrapper when executing commands with e.g. run. Must be able to exist in the form <env.shell> "<command goes here>" - e.g. the default uses Bash's -c option which takes a command string as its value.

See also
--shell, FAQ on bash as default shell, Execution model
"""


env.skip_bad_hosts = False
"""
Default: False

If True, causes fab (or non-fab use of execute) to skip over hosts it can't connect to.

New in version 1.4.

See also
--skip-bad-hosts, Excluding specific hosts, Execution model
"""


env.ssh_config_path = '$HOME/.ssh/config'
"""
Default: $HOME/.ssh/config

Allows specification of an alternate SSH configuration file path.

New in version 1.4.

See also
--ssh-config-path, Leveraging native SSH config files
"""


env.ok_ret_codes = [0]
"""
Default: [0]

Return codes in this list are used to determine whether calls to run/sudo/sudo are considered successful.

New in version 1.6.
"""


#env.sudo_prefix
"""
Default: "sudo -S -p '%(sudo_prompt)s' " % env

The actual sudo command prefixed onto sudo calls' command strings. Users who do not have sudo on their default remote $PATH, or who need to make other changes (such as removing the -p when passwordless sudo is in effect) may find changing this useful.

See also
The sudo operation; env.sudo_prompt
"""


#env.sudo_prompt
"""
Default: "sudo password:"

Passed to the sudo program on remote systems so that Fabric may correctly identify its password prompt.

See also
The sudo operation; env.sudo_prefix
"""


env.sudo_user = None
"""
Default: None

Used as a fallback value for sudo's user argument if none is given. Useful in combination with settings.

See also
sudo
"""


env.tasks = []
"""
Default: []

Set by fab to the full tasks list to be executed for the currently executing command. For informational purposes only.

See also
Execution model
"""


env.timeout = 10
"""
Default: 10

Network connection timeout, in seconds.

New in version 1.4.

See also
--timeout, connection_attempts
"""


env.use_shell = True
"""
Default: True

Global setting which acts like the use_shell argument to run/sudo: if it is set to False, operations will not wrap executed commands in env.shell.
"""


env.use_ssh_config = False
"""
Default: False

Set to True to cause Fabric to load your local SSH config file.

New in version 1.4.

See also
Leveraging native SSH config files
"""


#env.user
"""
Default: User's local username

The username used by the SSH layer when connecting to remote hosts. May be set globally, and will be used when not otherwise explicitly set in host strings. However, when explicitly given in such a manner, this variable will be temporarily overwritten with the current value - i.e. it will always display the user currently being connected as.

To illustrate this, a fabfile:

from fabric.api import env, run

env.user = 'implicit_user'
env.hosts = ['host1', 'explicit_user@host2', 'host3']

def print_user():
    with hide('running'):
        run('echo "%(user)s"' % env)
and its use:

$ fab print_user

[host1] out: implicit_user
[explicit_user@host2] out: explicit_user
[host3] out: implicit_user

Done.
Disconnecting from host1... done.
Disconnecting from host2... done.
Disconnecting from host3... done.
As you can see, during execution on host2, env.user was set to "explicit_user", but was restored to its previous value ("implicit_user") afterwards.

Note
env.user is currently somewhat confusing (it's used for configuration and informational purposes) so expect this to change in the future - the informational aspect will likely be broken out into a separate env variable.

See also
Execution model, --user
"""


#env.version
"""
Default: current Fabric version string

Mostly for informational purposes. Modification is not recommended, but probably won't break anything either.

See also
--version
"""


env.warn_only = False
"""
Default: False

Specifies whether or not to warn, instead of abort, when run/sudo/local encounter error conditions.
"""



























"""
env.

env.roledefs = {'role1': ['b', 'c']}
# For example, code talking to an HTTP API, or a database, or ...
from mylib import external_datastore

# This is the actual algorithm involved. It does not care about host
# lists at all.
def do_work():
    run("something interesting on a host")

# This is the user-facing task invoked on the command line.
@task
def deploy(lookup_param):
    # This is the magic you don't get with @hosts or @roles.
    # Even lazy-loading roles require you to declare available roles
    # beforehand. Here, the sky is the limit.
    host_list = external_datastore.query(lookup_param)
    # Put this dynamically generated host list together with the work to be
    # done.
    execute(do_work, hosts=host_list)




"""