#!/usr/bin/env python
import optparse
import os.path
from git import Repo
from git import InvalidGitRepositoryError
import shutil
import logging



def clean_up(working_dir):
    if os.path.exists(working_dir):
        logging.info("clean up " + working_dir)
        shutil.rmtree(working_dir)

def get_working_dir(checkout_dir, use_prefix, repository, commit_hash):
    if commit_hash == "HEAD":
        return repository

    working_dir = checkout_dir
    if use_prefix:
        prefix =  os.path.basename(repository)
        working_dir +=  "/"+ prefix + "_" + commit_hash
    else:
        working_dir +=  "/" + commit_hash   
    return working_dir


def get_commit_message(commit):
    return "Commit: %s \nAuthor: %s \nDate: %s\n\t%s" % (commit,
            commit.author, commit.committed_datetime, commit.message)

def main():
  logging.getLogger().setLevel(logging.INFO)
  p = optparse.OptionParser()
  p.add_option('--repository', '-r', help="path to the repository")
  p.add_option('--checkout-dir', '-d', default="/tmp/",
    help="base path for checkouts")
  p.add_option('--commit-hash', '-c',
    help="the commit hash to be checked out")
  p.add_option('--use-prefix', action="store_true", dest="use_prefix", 
    help="prepend the dirname of the repository to the checkout_dir")
  p.add_option('--get-path', action="store_true", 
    dest="get_path", 
    help="only return the path where the code would be. useful for cli")
  options, arguments = p.parse_args()

  if options.repository is None:
    logging.error("repository required")
    return
  if options.commit_hash is None:
    logging.error("commit-hash required")
    return

  if options.get_path:
    print(get_working_dir(options.checkout_dir, options.use_prefix, options.repository, options.commit_hash))
    return

  if options.commit_hash == "HEAD":
      # do nothing for commit HEAD
      return

  if os.path.exists(options.checkout_dir):
    working_dir = get_working_dir(options.checkout_dir, options.use_prefix, options.repository, options.commit_hash)

    if not os.path.exists(working_dir):
      logging.info("checkout repository " + options.repository + " to " + working_dir)
      os.system("git clone " + options.repository + " " + working_dir)
    else:
      logging.info("directory " + working_dir + " already exists.") 

    try:
      logging.info("check if  " + working_dir + " is git repository.") 
      repo = Repo(working_dir)
      assert not repo.bare
      try:
        logging.info("try checking out  " + options.commit_hash)
        repo.head.reference = repo.commit(options.commit_hash)
        message = get_commit_message(repo.head.commit)
        logging.info(message)
        repo.git.reset('--hard')
        logging.info("successfull")

      except ValueError as e:
        logging.info("Commit " + options.commit_hash + " invalid")
        clean_up(working_dir)
    except InvalidGitRepositoryError as e:
        logging.info(working_dir + " is not a valid repository")   
  else:
    logging.info("checkout dir " + options.checkout_dir + " does not exist")


 
if __name__ == '__main__':
  main()
