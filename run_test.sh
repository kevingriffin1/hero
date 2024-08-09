
export HERO_ENV="dev"
export HERO_PROJECT="dfw-app"
export HERO_CLIENT_ID="6mhtmeq8ailaecpmvd6lj23ico"
export HERO_CLIENT_SECRET="c70ktei98trjl3q5j4cn626a61226mfl1qq2rkfna29mip85vaa"

pytest  -s -v test/test_data_repo.py

unset HERO_ENV
unset HERO_PROJECT
unset HERO_CLIENT_ID
unset HERO_CLIENT_SECRET
