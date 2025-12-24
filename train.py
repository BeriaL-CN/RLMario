#正式训练文件
import os
import uuid
from gym.wrappers import GrayScaleObservation, ResizeObservation
from util_class import SkipFrame
from stable_baselines3 import PPO
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack

# 创建环境的函数
def make_env():
    env = gym_super_mario_bros.make('SuperMarioBros-v0')
    #限制动作空间
    env = JoypadSpace(env, SIMPLE_MOVEMENT)
    #简化observation
    #帧跳跃
    env = SkipFrame(env, 4)
    #灰度化
    env = GrayScaleObservation(env, keep_dim=True)
    #调整尺寸
    env = ResizeObservation(env, shape=(84, 84))
    return env


env = make_env()

# 监控器，记录训练数据，保存到monitor_log文件夹，每次运行生成一个新的文件
monitor_dir = r'./monitor_log/'
os.makedirs(monitor_dir, exist_ok=True)
env = Monitor(env, filename=os.path.join(monitor_dir, str(uuid.uuid4())))

env = DummyVecEnv([lambda: env])  # 使用DummyVecEnv包装环境,以兼容stable-baselines3的接口要求
env = VecFrameStack(env, 4, channels_order='last')  # 帧叠加,叠加4帧,用于捕捉动态信息

model = PPO(policy='CnnPolicy', env=env, verbose=1, tensorboard_log=r'./tensorboard_log/')
model.learn(total_timesteps=10000)
model.save('ppo_mario')

env.close()
