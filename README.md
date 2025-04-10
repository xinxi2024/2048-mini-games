# 2048 游戏

这是一个使用 HTML5、CSS3 和 JavaScript 实现的 2048 游戏。支持多种游戏模式和皮肤主题。

## 特性

- 多种游戏模式：
  - 普通模式：经典 2048 玩法
  - 时间挑战模式：1分钟、5分钟、10分钟限时挑战
- 多种皮肤主题：
  - 默认皮肤
  - 暗黑模式
  - 霓虹风格
  - 木质风格
- 音效系统
- 分数记录
- 自动保存皮肤设置

## 项目结构

```
2048-static/
├── index.html          # 主页面
├── css/               # 样式文件
│   ├── style.css      # 主样式
│   └── skins.css      # 皮肤样式
├── js/                # JavaScript 文件
│   ├── game.js        # 游戏核心逻辑
│   ├── audio.js       # 音效系统
│   └── ui.js          # 界面交互
├── assets/            # 资源文件
│   └── sounds/        # 音效文件
└── netlify.toml       # Netlify 配置文件
```

## 本地运行

1. 使用本地服务运行index.html即可


## 游戏操作

- 使用方向键（↑↓←→）移动方块
- 点击"新游戏"按钮开始新游戏
- 在下拉菜单中选择不同的皮肤主题
- 点击模式按钮切换游戏模式

## 浏览器支持

- Chrome (推荐)
- Firefox
- Safari
- Edge

## 开发说明

如需修改游戏：

1. 游戏逻辑在 `js/game.js`
2. 界面交互在 `js/ui.js`
3. 音效系统在 `js/audio.js`
4. 皮肤样式在 `css/skins.css`

## License

MIT License 