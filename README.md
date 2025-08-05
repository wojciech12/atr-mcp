## Template

1. `~/.claude/settings.json`:

   ```json
   "includeCoAuthoredBy": false
   ```

2. Voice notifications, requirements:
   - piper - [github](https://github.com/rhasspy/piper/releases) + [voice](https://rhasspy.github.io/piper-samples/) (I use `en_US-libritts_r-medium`)
   - ffmpeg package for `ffpg`
   - set `PIPER_HOME` env variable
   - hooks scripts assumes that the model is `$PIPER_HOME/models`

3. TBA
