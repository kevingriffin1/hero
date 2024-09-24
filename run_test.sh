
export HERO_ENV="dev"
export HERO_PROJECT="hero-test-framework"
export HERO_CLIENT_ID="306m74pgmccj9qd1ccb876fdgk"
export HERO_CLIENT_SECRET="u21676f1mrcqmhh5m723l1og4urjbjjg0oir37d4k2j7frpa9i0"

# Note: due to network latency, the tests may fail if the server(s) is(are) too slow to respond
# In that case, try running the tests again

# run all the things
pytest test
# Or just run a single suite/collection
# pytest -s -v test/test_auth.py

unset HERO_ENV
unset HERO_PROJECT
unset HERO_CLIENT_ID
unset HERO_CLIENT_SECRET
