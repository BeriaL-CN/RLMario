# RLMario — Reinforcement Learning: Super Mario (Stable-Baselines3)

This repository is a personal implementation of the Super Mario reinforcement-learning project shown in a Bilibili tutorial. The implementation uses the `stable-baselines3` framework together with the Gym Super Mario environment.

## Original Tutorial & Repository
- Video project GitHub: <https://github.com/jusway/RL_SuperMario/>

## References
- Gym Super Mario Bros: Ito, K., & Hosoda, K.; "gym-super-mario-bros" — adapted Gym environment for Super Mario Bros. Package & docs: https://github.com/Kautenja/gym-super-mario-bros
- NES emulator backend (nes-py): https://github.com/Kautenja/nes-py


## Dependencies & Installation
- Dependencies are listed in `requirements.txt`. Please install Conda and the appropriate Python version first (see the original video for details).

```powershell
pip install -r requirements.txt
```

- `requirements.txt` specifies the package versions required by this project.

## Notes
- This repository is a personal implementation for learning and reference only. Verify dependency compatibility before using in production.

---

# RLMario — 强化学习：超级马里奥（Stable-Baselines3）

本项目是基于 B 站教程的超级马里奥强化学习个人实现，使用 `stable-baselines3` 框架和对应的 `gym` 游戏包。

## 原教程与仓库
- 视频项目 GitHub：<https://github.com/jusway/RL_SuperMario/>

## 参考与引用
- `gym-super-mario-bros`：由 Kautenja 开发，提供 Super Mario Bros 的 Gym 环境（仓库与文档：https://github.com/Kautenja/gym-super-mario-bros）
- NES 模拟器后端 `nes-py`（仓库：https://github.com/Kautenja/nes-py）

## 依赖与安装
- 本项目的依赖列在 `requirements.txt` 中。请先安装 Conda 和对应的 Python 版本（详见源视频），然后运行：

```powershell
pip install -r requirements.txt
```

- `requirements_explained.txt` 用于详细解释依赖问题，请务必查看。

## TensorBoard

To view training logs with TensorBoard, make sure TensorBoard is installed in the same Python environment you use to run training (it's already listed in `requirements.txt`). You can start it in two ways:

- Directly with Python (recommended if `tensorboard` CLI is not on PATH):

```powershell
python -m tensorboard --logdir=logs --port=6006
```

- Or use the provided PowerShell helper script (activate your environment first):

```powershell
.\scripts\start_tensorboard.ps1
```

If you still see "The term 'tensorboard' is not recognized", activate your virtual environment or conda environment before running the script:

```powershell
# venv
.\venv\Scripts\Activate.ps1

# conda
conda activate <env-name>
```

## TensorBoard

如需查看训练日志，请确保在训练所使用的 Python 环境中安装了 TensorBoard（`requirements.txt` 中已列出）。可通过两种方式启动：

- 直接使用 Python 模块（若 `tensorboard` CLI 不在 PATH 中，推荐此法）：

```powershell
python -m tensorboard --logdir=logs --port=6006
```

- 或使用仓库提供的 PowerShell 启动脚本（先激活环境）：

```powershell
.\scripts\start_tensorboard.ps1
```

如果仍出现 “The term 'tensorboard' is not recognized” 错误，请在运行脚本前激活你的 virtualenv 或 conda 环境：

```powershell
# venv
.\venv\Scripts\Activate.ps1

# conda
conda activate <env-name>
```
## 说明
- 本仓库为个人实现，仅供学习与参考。若基于本项目开展工作，请注意依赖版本兼容性。