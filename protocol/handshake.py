"""handshake 核心模块（初始失败环境，待修复）。"""

def nonce_fresh(nonce, seen):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def sequence_valid(seq, last):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def session_alive(expiry, now):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def transition_allowed(state, event):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def credential_isolated(cred, layer):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def build_handshake(client_nonce, server_nonce):
    """待实现的安全修复入口。"""
    raise NotImplementedError
