# study_streamlit

repo for study Streamlit

## Dependency

- python 3.13
- uv

## Auth

- `.streamlit/secrets.toml` sample

```ini
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

## Reference

- [Streamlit user auth concept](https://docs.streamlit.io/develop/concepts/connections/authentication)
- [Streamlit Google OICD tutorial](https://docs.streamlit.io/develop/tutorials/authentication/google)
- [`st.user` API reference](https://docs.streamlit.io/develop/api-reference/user/st.user)
- [Streamlit login/logout sample](https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation)
