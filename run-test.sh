export HERO_ENV="dev"
export HERO_PROJECT="aeroportal-app"
export HERO_CLIENT_ID="306m74pgmccj9qd1ccb876fdgk"
export HERO_CLIENT_SECRET="u21676f1mrcqmhh5m723l1og4urjbjjg0oir37d4k2j7frpa9i0"
# export HERO_RESILIENT_SESSION=true
# export HERO_ML_MODEL_REGISTRY_URL="http://localhost:8010/m3s/api/v1"

poetry run pytest -s

unset HERO_ENV
unset HERO_PROJECT
unset HERO_CLIENT_ID
unset HERO_CLIENT_SECRET
# unset HERO_RESILIENT_SESSION