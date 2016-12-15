import subprocess as sp
import logging

logger = logging.getLogger('pelicangit')

class GitRepo:
    def __init__(self, repoDir, origin, master, is_local_dir=False):
        self.repoDir = repoDir
        self.origin = origin
        self.master = master
        self.originMaster = origin + '/' + master
        self.is_local_dir = is_local_dir

    def log(self, args):
        self.git_exec('log', args)

    def push(self, args):
        self.git_exec('push', args)

    def commit(self, message, args):
        self.git_exec('commit', args + ['-m', '"' + message + '"'])

    def add(self, args):
        self.git_exec('add', args)

    def rm(self, args):
        self.git_exec('rm', args)

    def fetch(self, args):
        self.git_exec('fetch', args)

    def reset(self, args):
        self.git_exec('reset', args)

    def log(self, args):
        return self.git_exec('log', args)

    def git_exec(self, firstArg, args):
        args.insert(0, firstArg)
        args.insert(0, 'git')

        output = sp.check_output(args, cwd=self.repoDir)
        logger.debug(output.decode())

        return output
