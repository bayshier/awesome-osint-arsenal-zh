#!/usr/bin/env bash
# ===================================================================
# Awesome OSINT Arsenal——总调度器
# awesome-osint-arsenal v2.1（统一生产版）的一部分
# 带错误处理地顺序执行各分类安装器。
# 支持最好：Kali / Debian / Ubuntu / Parrot。
# Partial: Arch / Manjaro / Fedora / RHEL.
# ===================================================================
set -uo pipefail

# 保持配色与日志格式与子模块一致
RED="\033[0;31m"
GRN="\033[0;32m"
YLW="\033[1;33m"
BLU="\033[0;34m"
CYN="\033[0;36m"
NC="\033[0m"

LOGFILE="${LOGFILE:-$HOME/osint-install-errors.log}"

# 核心环境守卫
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}[✗] error:${NC} This master orchestrator requires elevated privileges."
  echo "请以 root 运行: sudo bash $0"
  exit 1
fi

# 切换到脚本执行目录，安全解析相对路径
cd "$(dirname "$0")"

# 目标子模块
INSTALLERS=(
  "osint.sh"
  "redteam.sh"
  "blueteam.sh"
  "forensics.sh"
  "hardware.sh"
  "labs.sh"
  "extras.sh"
)

# 初始化/清空主错误日志
: >"$LOGFILE"

# 运行指标统计
START_TIME=$SECONDS
PASSED_MODULES=0
FAILED_MODULES=0
declare -ga UNABLE_TO_LOCATE=()

echo -e "${CYN}[i]${NC} Initializing Master Deployment Engine..."
echo -e "${CYN}[i]${NC} Runtime failures will be aggregated inside: $LOGFILE"

for inst in "${INSTALLERS[@]}"; do
  echo
  echo -e "${BLU}=======================================================${NC}"
  echo -e " 🚀 Launching Deployment Segment: ${CYN}$inst${NC}"
  echo -e "${BLU}=======================================================${NC}"
  
  # 防御性文件校验钩子
  if [ ! -f "$inst" ]; then
    echo -e "${YLW}[~] Skipping:${NC} Module script '$inst' not found in workspace directory."
    UNABLE_TO_LOCATE+=("$inst")
    FAILED_MODULES=$((FAILED_MODULES + 1))
    echo "总调度器错误：文件不存在: $inst"
    continue
  fi

  # 显式授予可执行权限，避免权限拒绝陷阱
  chmod +x "$inst"

  # 执行子 shell 层。导出 LOGFILE 保证子模块写入同一路径。
  export LOGFILE
  if bash "$inst"; then
    PASSED_MODULES=$((PASSED_MODULES + 1))
  else
    echo -e "${RED}[✗] Failure warning:${NC} Module $inst returned a non-zero exit status."
    FAILED_MODULES=$((FAILED_MODULES + 1))
    echo "总调度器错误：子模块执行失败，来自: $inst"
  fi
done

# 统计执行耗时
ELAPSED_DURATION=$((SECONDS - START_TIME))
MINUTES=$((ELAPSED_DURATION / 60))
SECONDS_REM=$((ELAPSED_DURATION % 60))

# ===================================================================
# 主编译面板
# ===================================================================
echo
echo -e "${CYN}=======================================================${NC}"
echo -e " 🎉 GRAND ARCHITECTURE DEPLOYMENT COMPLETE"
echo -e "${CYN}=======================================================${NC}"
echo -e "  Total Active Script Modules Checked : $((PASSED_MODULES + FAILED_MODULES))"
echo -e "  Successful Module Deployments       : ${GRN}$PASSED_MODULES${NC}"
echo -e "  Unresolved/Failed Components        : ${RED}$FAILED_MODULES${NC}"
echo -e "  Total Provisioning Runtime          : ${YLW}${MINUTES}m ${SECONDS_REM}s${NC}"
echo -e "${CYN}=======================================================${NC}"

if [ ${#UNABLE_TO_LOCATE[@]} -gt 0 ]; then
  echo -e "${YLW}[!] Missing Components Reminder:${NC} ${UNABLE_TO_LOCATE[*]}"
  echo "确保所有配套模块脚本已检出到本工作目录。"
fi

if [ "$FAILED_MODULES" -gt 0 ]; then
  echo -e "${RED}[✗] Some installation routines requirements encountered friction.${NC}"
  echo -e "    Review explicit error codes and stack failures in: ${YLW}$LOGFILE${NC}"
else
  echo -e "${GRN}[✓] Core orchestration layers initialized clean with zero root exceptions.${NC}"
fi