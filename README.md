# 中国象棋 · 人机对弈（Fairy-Stockfish WASM + NNUE）

**线上版:** https://jz.github.io/xiangqi-ai/ （GitHub Pages + coi-serviceworker 注入 COOP/COEP）

引擎在**浏览器里**运行——纯静态页面，无后端。

- 引擎：[fairy-stockfish-nnue.wasm](https://github.com/fairy-stockfish/fairy-stockfish.wasm)（多线程 WASM 构建）
- 模型：`xiangqi-c07e94a5c7cb.nnue`（Pikafish 团队训练，较经典评估 +914 Elo，
  来自 [fairy-stockfish.github.io/nnue](https://fairy-stockfish.github.io/nnue/)）
- 规则/走法校验：[ffish-es6](https://www.npmjs.com/package/ffish-es6)（同项目的 Embind 库）

## 启动

```bash
cd ~/xiangqi-ai
python3 serve.py
# 浏览器打开 http://localhost:8766
```

必须经 `serve.py` 访问：多线程 WASM 依赖 SharedArrayBuffer，
需要 COOP/COEP 响应头（serve.py 已配置），直接 file:// 打开无效。

## 功能

- 执红/执黑（执黑自动翻转棋盘）、四档难度（Skill Level + 思考时间）
- 点选走子，显示合法落点；最后一手、将军提示、WXF 记谱着法列表
- 悔棋（撤销双方各一手）、深度/评分实时显示

## 部署到免费静态托管

页面纯静态，可部署到 Cloudflare Pages / Netlify（免费、不休眠），
只需让托管方发送两个响应头（两家都支持自定义头）：

```
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

GitHub Pages 不支持自定义响应头，不能用。

## 目录

- `index.html` — 棋盘 UI + 引擎驱动（UCI over postMessage）
- `lib/` — stockfish.js/.wasm/.worker.js、ffish.js/.wasm、xiangqi.nnue
- `serve.py` — 本地静态服务器（带 COOP/COEP 头）
- `vendor/` — npm 包原件与 Node 验证脚本（部署时不需要）
