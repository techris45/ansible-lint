.. include:: ../.github/CONTRIBUTING.rst
   :end-before: DO-NOT-REMOVE-deps-snippet-PLACEHOLDER

Module dependency graph
-----------------------

Extra care should be taken when considering adding any dependency. Removing
most dependencies on Ansible internals is desired as these can change
without any warning.

.. command-output:: pipdeptree -p ansible-lint

.. include:: ../.github/CONTRIBUTING.rst
   :start-after: DO-NOT-REMOVE-deps-snippet-PLACEHOLDER

Adding a new rule
-----------------

Writing a new rule is as easy as adding a single new rule, one that combines
**implementation, testing and documentation**.

One good example is MetaTagValidRule_ which can easily be copied in order
to create a new rule by following the steps below:

* Install test dependencies using ``pip install -r test-requirements.txt``. You
  may want to use a :doc:`virtual environment <python3:tutorial/venv>` for
  that.
* Use a short but clear class name, which must match the filename
* Pick an unused ``id``, the first number is used to determine rule section.
  Look at rules_ page and pick one that matches the best your new rule.
  see which one fits best.
* Be sure ``experimental`` tag is included. Any new rule must stay as
  experimental for at least two weeks until this tag is removed in next major
  release.
* Update all class level variables.
* Implement linting methods needed by your rule, these are those starting with
  ``match`` prefix. Implement only those you need. For the moment you will need
  to look at how similar rules were implemented to figure out what to do.
* Update the tests. It must have at least one test and likely also a negative
  match one.
* If the rule is task specific, it may be best to include a test to verify its
  use inside blocks as well.
* Optional: Run the rule specific tests ``tox -e py38-ansible29 -- -k NewRule``
  as this will run only tests unique to that rule.
* Run ``tox`` in order to run all ansible-lint tests. Adding a new rule can
  break some other tests. Update them if needed.
* Run ``ansible-lint -L`` and check that the rule description renders
  correctly.
* Build the docs using ``tox -e docs`` and check that the new rule is displayed
  correctly in them.
* Assure linting is passing with ``tox -e lint``.
* Make a commit that explains why the rule is added and that eventually
  closing an existing bug by including ``Fixes: #123`` in its description.
  Commit message should follow the 50/72 formatting rule.
* Open a draft pull-request. When CI/CD reports green, move the draft PR from
  draft to ready for review.

.. _MetaTagValidRule: https://github.com/ansible/ansible-lint/blob/master/lib/ansiblelint/rules/MetaTagValidRule.py
.. _rules: https://ansible-lint.readthedocs.io/en/latest/default_rules.html
