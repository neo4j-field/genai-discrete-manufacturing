# this script will update the genai-discrete-manufacturing repo with changes from upstream
# the only directory that is affected is ps_genai_agents/
# this will NOT commit changes
git fetch upstream
git checkout upstream/main -- ps_genai_agents/