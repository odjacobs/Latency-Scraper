# Latency Scraper
Simple website latency scraper written in Python and usable with Prometheus.
# Configuration
Configuration is done inside of config.json. Just follow the layout of [config-example.json](config-example.json)
# Running
```
gunicorn scrape:app
```
# License
This project is licensed under the GNU General Public License version 3.0. See [LICENSE](LICENSE) for details.
