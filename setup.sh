mkdir -p ~/.streamlit

echo "\
[server]\n\
headless = PORT\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
