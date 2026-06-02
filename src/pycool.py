#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__INFO__ = {
    'Obfuscator': 'PyCool', 
    'Obfuscator Owner': 'Trương Nhật Bảo Nam - ktn1703',
    'Github': 'https://github.com/Swp-dev/PyCool-Obufuscator',
    'Version': '1.0'
}

import ast, random, marshal, base64, bz2, zlib, lzma, sys, os
from ast import *

sys.setrecursionlimit(99999999)
ver = str(sys.version_info.major) + '.' + str(sys.version_info.minor)

try:
    from pystyle import *
except ModuleNotFoundError:
    os.system(f'pip{ver} install pystyle')
    from pystyle import *

System.Clear()

KTN_BANNER = r"""
  ██╗  ██╗████████╗███╗   ██╗
  ██║ ██╔╝╚══██╔══╝████╗  ██║
  █████╔╝    ██║   ██╔██╗ ██║
  ██╔═██╗    ██║   ██║╚██╗██║
  ██║  ██╗   ██║   ██║ ╚████║
  ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝
"""
print(Colorate.Diagonal(Colors.DynamicMIX((Col.cyan, Col.blue)), KTN_BANNER))
print(Colorate.Diagonal(Colors.DynamicMIX((Col.blue, Col.cyan)), '  KTN Obfuscator v3.0 — Unbreakable & Unreadable'))
print(Colorate.Diagonal(Colors.DynamicMIX((Col.cyan, Col.blue)), '  Dynamic Imports | Unicode Chaos | Hidden Anti-Class | AST Bytecode'))
print()

_STYLE = Colors.DynamicMIX((Col.cyan, Col.blue))

_HEX_CH  = '0123456789abcdef'
_HEX_EMO = ['🐉','🐲','⭐','✨','💫','⚡','🔥','💥','🌀','🥋','🥊','👊','🙌','👽','🤖','👺']
_E = dict(zip(_HEX_CH, _HEX_EMO))

def _raw_enc(s: str) -> str:
    return ''.join(_E[c] for c in s.encode().hex())

_KOR = [i for i in range(0xAC00, 0xD7A3) if chr(i).isprintable() and chr(i).isidentifier()]
_CHI = [i for i in range(0x4E00, 0x9FFF) if chr(i).isprintable() and chr(i).isidentifier()]
_JPN = [i for i in range(0x3040, 0x30FF) if chr(i).isprintable() and chr(i).isidentifier()]

def _vk(n=11): return ''.join(random.choices([chr(i) for i in _KOR], k=n))
def _vc(n=11): return ''.join(random.choices([chr(i) for i in _CHI], k=n))
def _vj(n=11): return ''.join(random.choices([chr(i) for i in _JPN], k=n))
def _vm(n=14): return ''.join(random.choices([chr(i) for i in (_KOR + _CHI + _JPN)], k=n))

def _names(*keys):
    used = set()
    out = {}
    for k in keys:
        while True:
            pool = random.choice([_KOR, _CHI, _JPN])
            n = random.randint(10, 18)
            v = ''.join(random.choices([chr(i) for i in pool], k=n))
            if v not in used:
                used.add(v)
                out[k] = v
                break
    return out

def _cjk_str(n=80):
    return ''.join(chr(random.randint(0x4E00, 0x9FFF)) for _ in range(n))

def _out_junk(count=250):
    lines = []
    for _ in range(count):
        ch = random.randint(0, 13)
        v1 = _vm(random.randint(12, 28))
        v2 = _vm(random.randint(8, 18))
        v3 = _vm(random.randint(8, 18))
        n1 = random.randint(2, 120)
        n2 = random.randint(0, 9999)
        n3 = random.randint(1, 255)
        n4 = random.randint(2, 15)

        if ch == 0:
            lines.append(f'{v1} = [{n2} for _ in range({n1})]')
        elif ch == 1:
            lines.append(f'{v1} = {{(lambda {v2}: {v2} ^ {n3})(i) for i in range({n1})}}')
        elif ch == 2:
            lines.append(f'{v1} = [(lambda {v2}, {v3}: {v2} * {v3})(i, j) for i in range({n1}) for j in range({n4})]')
        elif ch == 3:
            lines.append(f'{v1} = lambda {v2}: {v2} * {n2} + {n3}')
        elif ch == 4:
            inner = random.randint(2, 18)
            outer = random.randint(2, 12)
            lines.append(f'{v1} = [[(lambda {v2}: {v2} ^ {n3})(i) for i in range({inner})] for j in range({outer})]')
        elif ch == 5:
            lines.append(f'{v1} = [(lambda {v2}: {v2})({n2}) for _ in range({n1})]')
        elif ch == 6:
            cjk = _cjk_str(random.randint(80, 220))
            lines.append(f"'''\n{cjk}\n'''")
        elif ch == 7:
            cjk = _cjk_str(random.randint(40, 100))
            lines.append(f'# {cjk}')
        elif ch == 8:
            lines.append(f'{v1} = (lambda {v2}: (lambda {v3}: {v3} ^ {n3})({v2} + {n2}))({n1})')
        elif ch == 9:
            lines.append(f'{v1} = {{{n2} ^ i for i in range({n1})}}')
        elif ch == 10:
            lines.append(f'{v1} = lambda {v2}: lambda {v3}: {v2} * {n3} ^ {v3} + {n2}')
        elif ch == 11:
            lines.append(f'{v1} = [(lambda {v2}: {v2} + {n3})(i) for i in range({n1}) for j in range({n4})]')
        elif ch == 12:
            rows = random.randint(2, 8)
            cols = random.randint(2, 12)
            lines.append(f'{v1} = {{(lambda {v2}: {v2} ^ {n3})(i) for i in range({rows} * {cols})}}')
        else:
            lines.append(f'{v1} = {n2} ^ {n3} * {random.randint(1, 100)} + {random.randint(0, 9999)}')
    return '\n'.join(lines)

_ANTI_HOOK_SRC = """
import sys as _ah_s_
if str(print)  != '<built-in function print>':  _ah_s_.exit('KTN: hooked')
if str(exec)   != '<built-in function exec>':   _ah_s_.exit('KTN: hooked')
if str(eval)   != '<built-in function eval>':   _ah_s_.exit('KTN: hooked')
if str(input)  != '<built-in function input>':  _ah_s_.exit('KTN: hooked')
if str(len)    != '<built-in function len>':    _ah_s_.exit('KTN: hooked')
if str(_ah_s_.exit) != '<built-in function exit>': _ah_s_.exit('KTN: hooked')
try:
    import marshal as _ah_m_
    if str(_ah_m_.loads) != '<built-in function loads>': _ah_s_.exit('KTN: hooked')
except: pass
"""

_ANTI_DEBUG_SRC = """
import sys as _ad_s_, time as _ad_t_
if hasattr(_ad_s_, 'gettrace') and _ad_s_.gettrace() is not None: _ad_s_.exit('KTN: traced')
try:
    import debugpy; _ad_s_.exit('KTN: debugpy')
except ImportError: pass
_ad_t0_ = _ad_t_.perf_counter()
_ad_x_  = sum(range(50000))
if _ad_t_.perf_counter() - _ad_t0_ > 3.0: _ad_s_.exit('KTN: timing')
del _ad_t0_, _ad_x_
"""

_ANTI_VM_SRC = """
import sys as _av_s_, os as _av_o_, platform as _av_p_
_av_str_ = (_av_p_.node() + ' ' + _av_p_.processor() + ' ' + _av_p_.machine()).lower()
for _av_kw_ in ['vmware','virtualbox','vbox','qemu','hyper-v','xen','kvm']:
    if _av_kw_ in _av_str_: _av_s_.exit('KTN: vm')
if _av_o_.path.exists('/proc/scsi/scsi'):
    with open('/proc/scsi/scsi') as _av_f_:
        _av_sc_ = _av_f_.read().lower()
        for _av_kw_ in ['vmware','vbox','qemu']:
            if _av_kw_ in _av_sc_: _av_s_.exit('KTN: vm scsi')
try:
    import psutil as _av_ps_
    if _av_ps_.virtual_memory().total < 2*1024**3: _av_s_.exit('KTN: low ram')
    if (_av_ps_.cpu_count() or 0) < 2: _av_s_.exit('KTN: low cpu')
    _av_bad_ = ['vmtoolsd','vboxservice','qemu-ga','vmwaretray','vboxclient']
    _av_prs_ = [p.name().lower() for p in _av_ps_.process_iter(['name'])]
    for _av_bp_ in _av_bad_:
        if _av_bp_ in _av_prs_: _av_s_.exit('KTN: vm proc')
except ImportError: pass
"""

_ANTI_PROXY_SRC = """
import sys as _ap_s_, os as _ap_o_
for _ap_e_ in ['HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','ALL_PROXY','all_proxy']:
    _ap_v_ = _ap_o_.environ.get(_ap_e_, '').lower()
    if 'burp' in _ap_v_ or 'fiddler' in _ap_v_ or 'mitm' in _ap_v_ or '8080' in _ap_v_ or '8888' in _ap_v_ or 'proxyman' in _ap_v_ or 'httptoolkit' in _ap_v_:
        _ap_s_.exit('KTN: proxy')
try:
    import urllib.request as _ap_u_
    _ap_op_ = _ap_u_.build_opener()
    if len(_ap_op_.handlers) > 6: _ap_s_.exit('KTN: urllib patched')
except: pass
"""

def _build_anti_src(do_hook, do_debug, do_vm, do_proxy):
    parts = []
    if do_hook:  parts.append(_ANTI_HOOK_SRC)
    if do_debug: parts.append(_ANTI_DEBUG_SRC)
    if do_vm:    parts.append(_ANTI_VM_SRC)
    if do_proxy: parts.append(_ANTI_PROXY_SRC)
    return '\n'.join(parts)

def _chr_ords(s):
    return list(ord(c) for c in s)

def _dyn_import(module_name):
    ords = list(ord(c) for c in module_name)
    return f"__import__(''.join(map(chr,{ords})))"

def _ast_arg(name):
    return ast.arguments(posonlyargs=[], args=[ast.arg(arg=name)],
        vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])

def _ast_junk():
    v1, v2, v3 = _vk(), _vk(), _vk()
    t = random.randint(0, 9)
    if t == 0:
        return ast.Assign(
            targets=[ast.Name(v1, ast.Store())],
            value=ast.ListComp(
                ast.BinOp(ast.Name(v2, ast.Load()), ast.BitXor(), ast.Constant(random.randint(1,255))),
                [ast.comprehension(ast.Name(v2, ast.Store()),
                    ast.Call(ast.Name('range',ast.Load()),[ast.Constant(random.randint(10,60))],[]),
                    [],0)]), lineno=0)
    elif t == 1:
        return ast.Assign(
            targets=[ast.Name(v1, ast.Store())],
            value=ast.DictComp(
                ast.Name(v2, ast.Load()),
                ast.BinOp(ast.Name(v2,ast.Load()),ast.Mult(),ast.Constant(random.randint(2,99))),
                [ast.comprehension(ast.Name(v2,ast.Store()),
                    ast.Call(ast.Name('range',ast.Load()),[ast.Constant(random.randint(5,30))],[]),
                    [],0)]), lineno=0)
    elif t == 2:
        return ast.Assign(targets=[ast.Name(v1,ast.Store())],
            value=ast.List([ast.Constant(random.randint(0,9999)) for _ in range(random.randint(5,20))],ast.Load()),
            lineno=0)
    elif t == 3:
        return ast.Assign(targets=[ast.Name(v1,ast.Store())],
            value=ast.Lambda(_ast_arg(v2),
                ast.BinOp(ast.Name(v2,ast.Load()),ast.Add(),ast.Constant(random.randint(1,9999)))),
            lineno=0)
    elif t == 4:
        return ast.For(ast.Name(v1,ast.Store()),
            ast.Call(ast.Name('range',ast.Load()),[ast.Constant(0)],[]),
            [ast.Pass()],[],lineno=0)
    elif t == 5:
        n = random.randint(100,9999)
        return ast.Assign(targets=[ast.Name(v1,ast.Store())],
            value=ast.BinOp(ast.BinOp(ast.Constant(n*7),ast.BitXor(),ast.Constant(n*3)),
                ast.Add(),ast.Constant(random.randint(0,255))), lineno=0)
    elif t == 6:
        return ast.Assign(targets=[ast.Name(v1,ast.Store())],
            value=ast.Lambda(_ast_arg(v2),ast.Lambda(_ast_arg(v3),
                ast.BinOp(ast.Name(v2,ast.Load()),ast.Mult(),ast.Name(v3,ast.Load())))),
            lineno=0)
    elif t == 7:
        rows,cols = random.randint(2,5),random.randint(2,8)
        return ast.Assign(targets=[ast.Name(v1,ast.Store())],
            value=ast.ListComp(
                ast.ListComp(
                    ast.BinOp(ast.Name(v2,ast.Load()),ast.BitXor(),ast.Constant(random.randint(1,127))),
                    [ast.comprehension(ast.Name(v2,ast.Store()),
                        ast.Call(ast.Name('range',ast.Load()),[ast.Constant(cols)],[]),
                        [],0)]),
                [ast.comprehension(ast.Name(v3,ast.Store()),
                    ast.Call(ast.Name('range',ast.Load()),[ast.Constant(rows)],[]),
                    [],0)]), lineno=0)
    elif t == 8:
        return ast.Assign(targets=[ast.Name(v1,ast.Store())],
            value=ast.Set([ast.Constant(random.randint(0,9999)) for _ in range(random.randint(3,12))]),
            lineno=0)
    else:
        return ast.Assign(targets=[ast.Name(v1,ast.Store())],
            value=ast.Constant(random.choice([True,False,None,'',0,1,-1])), lineno=0)

def _ast_many(n=18): return [_ast_junk() for _ in range(n)]

def _ast_wrap(node):
    return [
        *_ast_many(random.randint(8,18)),
        ast.Try(
            body=[ast.Expr(ast.Tuple([ast.BinOp(ast.Constant(1),ast.Div(),ast.Constant(0))],ast.Load()))],
            handlers=[ast.ExceptHandler(body=[node])],
            orelse=[], finalbody=[]),
        *_ast_many(random.randint(5,12)),
    ]

_BUILTINS = [
    '__import__','abs','all','any','ascii','bin','breakpoint','callable','chr',
    'compile','delattr','dir','divmod','eval','exec','format','getattr','globals',
    'hasattr','hash','hex','id','input','isinstance','issubclass','iter','len',
    'locals','max','min','next','oct','ord','pow','print','repr','round','setattr',
    'sorted','sum','vars','None','Ellipsis','NotImplemented','False','True','bool',
    'memoryview','bytearray','bytes','classmethod','complex','dict','enumerate',
    'filter','float','frozenset','int','list','map','object','open','property',
    'range','reversed','set','slice','staticmethod','str','super','tuple','type','zip',
]

class _FStrFix(ast.NodeTransformer):
    def visit_JoinedStr(self, node):
        parts = []
        for val in node.values:
            if isinstance(val, ast.Constant):
                parts.append(val)
            elif isinstance(val, ast.FormattedValue):
                inner = val.value
                fn = {115:'str',114:'repr',97:'ascii'}.get(val.conversion,'str')
                inner = ast.Call(ast.Name(fn,ast.Load()),[inner],[])
                parts.append(inner)
            else:
                parts.append(ast.Call(ast.Name('str',ast.Load()),[val],[]))
        if not parts: return ast.Constant('')
        if len(parts)==1 and isinstance(parts[0],ast.Constant): return parts[0]
        return ast.Call(ast.Attribute(ast.Constant(''),'join',ast.Load()),
                        [ast.Tuple(parts,ast.Load())],[])

class _HideBuiltins(ast.NodeTransformer):
    def __init__(self, imp_name='_ktn_imp_'):
        self._imp = imp_name
    def visit_Name(self, node):
        if node.id in _BUILTINS:
            return ast.Call(ast.Name('getattr',ast.Load()),
                [ast.Call(ast.Name(self._imp,ast.Load()),[ast.Constant('builtins')],[]),
                 ast.Constant(node.id)],[])
        return node

def _mk_obfstr(s):
    if not s: return ast.Constant('')
    v = _vk()
    lst = [ord(c) for c in s]
    lam3 = ast.Lambda(_ast_arg(_vk()),
        ast.Call(ast.Attribute(ast.Call(ast.Name('str',ast.Load()),[],[]),'join',ast.Load()),
            [ast.GeneratorExp(
                ast.Call(ast.Name('chr',ast.Load()),[ast.Name(v,ast.Load())],[]),
                [ast.comprehension(ast.Name(v,ast.Store()),
                    ast.List([ast.Constant(x) for x in lst],ast.Load()),[],0)])],[]))
    lam2 = ast.Lambda(_ast_arg(_vk()), ast.Call(lam3,[ast.Constant(0)],[]))
    lam1 = ast.Lambda(_ast_arg(_vk()), ast.Call(lam2,[ast.Constant(0)],[]))
    return ast.Call(lam1,[ast.Constant(0)],[])

def _mk_obfint(i):
    offset = random.randint(1000,99999)
    lam3 = ast.Lambda(_ast_arg(_vk()),
        ast.Call(ast.Name('int',ast.Load()),
            [ast.BinOp(ast.Constant(i+offset),ast.Sub(),ast.Constant(offset))],[]))
    lam2 = ast.Lambda(_ast_arg(_vk()), ast.Call(lam3,[ast.Constant(0)],[]))
    lam1 = ast.Lambda(_ast_arg(_vk()), ast.Call(lam2,[ast.Constant(0)],[]))
    return ast.Call(lam1,[ast.Constant(0)],[])

class _ObfConst(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value,str) and node.value:
            return _mk_obfstr(node.value)
        elif isinstance(node.value,int) and not isinstance(node.value,bool) and node.value!=0:
            return _mk_obfint(node.value)
        return node

class _AddJunk(ast.NodeTransformer):
    def _proc(self, body):
        out = []
        for s in body: out.extend(_ast_wrap(s))
        return out
    def visit_Module(self, node):
        for s in node.body:
            if isinstance(s,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): self.visit(s)
        node.body = self._proc(node.body)
        return node
    def visit_FunctionDef(self, node):
        node.body = self._proc(node.body)
        return node
    def visit_ClassDef(self, node):
        node.body = self._proc(node.body)
        return node

def _xor_b(data, key): return bytes(b^key[i%len(key)] for i,b in enumerate(data))

def _rc4(data, key):
    S=list(range(256)); j=0
    for i in range(256):
        j=(j+S[i]+key[i%len(key)])%256; S[i],S[j]=S[j],S[i]
    i=j=0; out=[]
    for b in data:
        i=(i+1)%256; j=(j+S[i])%256; S[i],S[j]=S[j],S[i]
        out.append(b^S[(S[i]+S[j])%256])
    return bytes(out)

def _roll_xor(data, seed):
    out=bytearray(); state=seed&0xFFFFFFFFFFFFFFFF
    for b in data:
        state=(state*6364136223846793005+1442695040888963407)&0xFFFFFFFFFFFFFFFF
        out.append(b^(state&0xFF))
    return bytes(out)

def _shuffle(data, seed):
    lst=list(data); rng=random.Random(seed)
    idx=list(range(len(lst))); rng.shuffle(idx)
    out=[0]*len(lst)
    for ni,oi in enumerate(idx): out[ni]=lst[oi]
    return bytes(out), idx

def _build_output_file(
    do_hook, do_debug, do_vm, do_proxy, do_hide,
    payload_repr, xor_key, rc4_key, shuffle_seed, rolling_seed, indices,
    imp_fn_name=None
):
    N = _names(
        'anti_cls','boot_cls','dec_cls',
        'va','vb',
        'ev','str_','bytes_','int_','dec_fn','imp_','exec_',
        'hex_emo_v','hex_ch_v','e2h_v','dec_arg','hx_v','ci_v','el_v',
        'p_v','xk_v','rs_v','rk_v','ss_v','idx_v',
        'rc4_m','roll_m','xor_m','uns_m','run_m',
        'S_v','j_v','i_v','o_v','b_v','k_v','d_v','seed_v','state_v',
        'ni_v','oi_v','b64_v','bz2_v','zl_v','lz_v','ma_v','dd_v',
        'err_v','tmp_v','tmp2_v',
    )

    hex_emo_repr = repr(_HEX_EMO)

    _sys_dyn  = _dyn_import('sys')
    _base64   = _dyn_import('base64')
    _bz2      = _dyn_import('bz2')
    _zlib     = _dyn_import('zlib')
    _lzma     = _dyn_import('lzma')
    _marshal  = _dyn_import('marshal')

    enc_import = _raw_enc('__tropmi__')
    enc_exec   = _raw_enc('cexe')

    any_anti = do_hook or do_debug or do_vm or do_proxy
    anti_src = _build_anti_src(do_hook, do_debug, do_vm, do_proxy)
    anti_ords = _chr_ords(anti_src) if any_anti else []

    anti_cls_code = ''
    if any_anti:
        anti_cls_code = f"""class {N['anti_cls']}:
    def __init__(self):
        eval(compile(''.join(map(chr,{anti_ords})),'<{_vm(6)}>','exec'))
    def __call__(self,*{N['va']},**{N['vb']}):self.__init__()
{N['anti_cls']}()
"""

    payload_imp = imp_fn_name if (imp_fn_name and do_hide) else N['imp_']
    ver_str  = ver
    extra_global = f',{payload_imp}' if (do_hide and payload_imp != N['imp_']) else ''
    extra_assign = f'        {payload_imp} = {N["imp_"]}\n' if (do_hide and payload_imp != N['imp_']) else ''
    boot_cls_code = f"""class {N['boot_cls']}:
    def __init__(self):
        {N['tmp_v']} = {_sys_dyn}
        {N['tmp2_v']} = str({N['tmp_v']}.version_info.major)+'.'+str({N['tmp_v']}.version_info.minor)
        if {N['tmp2_v']} != '{ver_str}': {N['tmp_v']}.exit('PyCool: need {ver_str}')
        print('>> Running...',end='\\r')
    def __call__(self,*{N['va']},**{N['vb']}):
        global {N['imp_']},{N['str_']},{N['bytes_']},{N['int_']},{N['dec_fn']},{N['exec_']}{extra_global}
        {N['ev']}    = eval('lave'[::-1])
        {N['str_']}  = {N['ev']}('rts'[::-1])
        {N['bytes_']}= {N['ev']}('setyb'[::-1])
        {N['int_']}  = {N['ev']}('tni'[::-1])
        {N['hex_emo_v']} = {hex_emo_repr}
        {N['hex_ch_v']}  = '0123456789abcdef'
        {N['e2h_v']}     = dict(zip({N['hex_emo_v']},{N['hex_ch_v']}))
        def {N['dec_fn']}({N['dec_arg']}):
            {N['hx_v']} = ''
            {N['ci_v']} = 0
            while {N['ci_v']} < len({N['dec_arg']}):
                for {N['el_v']} in {N['hex_emo_v']}:
                    if {N['dec_arg']}[{N['ci_v']}:{N['ci_v']}+len({N['el_v']})] == {N['el_v']}:
                        {N['hx_v']} += {N['e2h_v']}.get({N['el_v']},'')
                        {N['ci_v']} += len({N['el_v']}); break
                else: {N['ci_v']} += 1
            return {N['bytes_']}.fromhex({N['hx_v']}).decode()
        {N['imp_']}  = {N['ev']}({N['dec_fn']}('{enc_import}')[::-1])
        {N['exec_']} = {N['ev']}({N['dec_fn']}('{enc_exec}')[::-1])
{extra_assign}{N['boot_cls']}()()
"""

    dec_cls_code = f"""class {N['dec_cls']}:
    def __init__(self,*{N['va']}):
        self.{N['p_v']}   = {N['va']}[0]
        self.{N['xk_v']}  = {repr(xor_key)}
        self.{N['rs_v']}  = {repr(rolling_seed)}
        self.{N['rk_v']}  = {repr(rc4_key)}
        self.{N['idx_v']} = {repr(indices)}
    def {N['rc4_m']}(self,{N['d_v']},{N['k_v']}):
        {N['S_v']}=list(range(256));{N['j_v']}=0
        for {N['i_v']} in range(256):
            {N['j_v']}=({N['j_v']}+{N['S_v']}[{N['i_v']}]+{N['k_v']}[{N['i_v']}%len({N['k_v']})])%256
            {N['S_v']}[{N['i_v']}],{N['S_v']}[{N['j_v']}]={N['S_v']}[{N['j_v']}],{N['S_v']}[{N['i_v']}]
        {N['i_v']}={N['j_v']}=0;{N['o_v']}=[]
        for {N['b_v']} in {N['d_v']}:
            {N['i_v']}=({N['i_v']}+1)%256;{N['j_v']}=({N['j_v']}+{N['S_v']}[{N['i_v']}])%256
            {N['S_v']}[{N['i_v']}],{N['S_v']}[{N['j_v']}]={N['S_v']}[{N['j_v']}],{N['S_v']}[{N['i_v']}]
            {N['o_v']}.append({N['b_v']}^{N['S_v']}[({N['S_v']}[{N['i_v']}]+{N['S_v']}[{N['j_v']}])%256])
        return bytes({N['o_v']})
    def {N['roll_m']}(self,{N['d_v']},{N['seed_v']}):
        {N['o_v']}=bytearray();{N['state_v']}={N['seed_v']}&0xFFFFFFFFFFFFFFFF
        for {N['b_v']} in {N['d_v']}:
            {N['state_v']}=({N['state_v']}*6364136223846793005+1442695040888963407)&0xFFFFFFFFFFFFFFFF
            {N['o_v']}.append({N['b_v']}^({N['state_v']}&0xFF))
        return bytes({N['o_v']})
    def {N['xor_m']}(self,{N['d_v']},{N['k_v']}):
        return bytes({N['b_v']}^{N['k_v']}[{N['i_v']}%len({N['k_v']})] for {N['i_v']},{N['b_v']} in enumerate({N['d_v']}))
    def {N['uns_m']}(self,{N['d_v']}):
        {N['o_v']}=[0]*len({N['d_v']})
        for {N['ni_v']},{N['oi_v']} in enumerate(self.{N['idx_v']}): {N['o_v']}[{N['oi_v']}]={N['d_v']}[{N['ni_v']}]
        return bytes({N['o_v']})
    def {N['run_m']}(self):
        {N['b64_v']} = {_base64}
        {N['bz2_v']} = {_bz2}
        {N['zl_v']}  = {_zlib}
        {N['lz_v']}  = {_lzma}
        {N['ma_v']}  = {_marshal}
        {N['dd_v']} = {N['b64_v']}.b64decode(self.{N['p_v']})
        {N['dd_v']} = self.{N['roll_m']}({N['dd_v']},self.{N['rs_v']})
        {N['dd_v']} = self.{N['rc4_m']}({N['dd_v']},self.{N['rk_v']})
        {N['dd_v']} = self.{N['uns_m']}({N['dd_v']})
        {N['dd_v']} = self.{N['xor_m']}({N['dd_v']},self.{N['xk_v']})
        {N['dd_v']} = {N['b64_v']}.b85decode({N['dd_v']})
        {N['dd_v']} = {N['lz_v']}.decompress({N['dd_v']})
        {N['dd_v']} = {N['bz2_v']}.decompress({N['dd_v']})
        {N['dd_v']} = {N['zl_v']}.decompress({N['dd_v']})
        {N['dd_v']} = {N['zl_v']}.decompress({N['dd_v']})
        return {N['ma_v']}.loads({N['dd_v']})
"""

    exec_line = f"{N['exec_']}({N['dec_cls']}({payload_repr}).{N['run_m']}(),globals())"

    top_cjk   = '# ' + _cjk_str(200)
    top_cjk2  = '# ' + _cjk_str(150)

    j1 = _out_junk(320)   
    j2 = _out_junk(100)   
    j3 = _out_junk(120)   
    j4 = _out_junk(80)   

    output = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
{top_cjk}
{top_cjk2}
__OWN__= "Trương Nhật Bảo Nam - ktn1703",
__OBF__= "PyCool",
__VER__= "1.0",
__SRC__= "https://github.com/Swp-dev/PyCool-Obufuscator",
__CMT__ = "Don't Read This Code Because You Will Be Dizzy By My Magic!"

{j1}

{anti_cls_code}
{j2}

{boot_cls_code}
{j3}

{dec_cls_code}
{j4}

try:
    {exec_line}
except Exception as {N['err_v']}: print({N['err_v']})
except KeyboardInterrupt: exit('Exiting...')
"""
    return output

# main
def _ask(prompt):
    ans = input(Colorate.Diagonal(_STYLE, f'>> {prompt} (Y/n): ')).strip().lower()
    return ans != 'n'

def _step(msg):
    print(Colorate.Diagonal(_STYLE, f'[...] {msg}'))

def main():
    while True:
        path = input(Colorate.Diagonal(_STYLE, '>> Enter file path to obfuscate: ')).strip()
        try:
            with open(path,'r',encoding='utf-8') as f: src = f.read()
            break
        except FileNotFoundError:
            print(Colorate.Horizontal(Colors.red_to_white,'    File not found. Try again.\n'))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_white,f'    Error: {e}\n'))

    print()
    do_hide  = _ask('Hide builtins (recommended)')
    do_junk  = _ask('Add AST junk / dead code (recommended — extreme unreadability)')
    do_debug = _ask('Anti-debug (debugpy, pdb, trace hooks, timing attack)')
    do_vm    = _ask('Anti-VM / anti-sandbox (VMware, VBox, QEMU, low RAM/CPU)')
    do_hook  = _ask('Anti-hook (detect patched builtins, marshal, sys.exit)')
    do_proxy = _ask('Anti-proxy / anti-MITM (Burp, Fiddler, mitmproxy, HTTPToolkit)')
    print()

    _step('Parsing source...')
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        print(Colorate.Horizontal(Colors.red_to_white, f'    Syntax error: {e}')); return

    _step('Fixing f-strings...')
    _FStrFix().visit(tree); ast.fix_missing_locations(tree)

    imp_fn_name = _vm(random.randint(12, 18))

    if do_hide:
        _step('Hiding builtins via dynamic __import__...')
        _HideBuiltins(imp_fn_name).visit(tree); ast.fix_missing_locations(tree)

    _step('Obfuscating constants (strings + integers) with CJK lambda chains...')
    _ObfConst().visit(tree); ast.fix_missing_locations(tree)

    if do_junk:
        _step('Injecting AST junk / dead code with Korean/Chinese variable names...')
        _AddJunk().visit(tree); ast.fix_missing_locations(tree)

    _step('Compiling AST to bytecode...')
    try:
        unparsed = ast.unparse(tree)
        compiled = compile(unparsed, '<KTN>', 'exec')
        raw = marshal.dumps(compiled)
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f'    Compile error: {e}')); return

    _step('Multi-layer encryption: marshal→zlib×2→bz2→lzma→b85→XOR-32→shuffle→RC4→LCG-XOR→b64...')
    raw = zlib.compress(raw, 9)
    raw = zlib.compress(raw, 9)
    raw = bz2.compress(raw)
    raw = lzma.compress(raw)
    raw = base64.b85encode(raw)

    xor_key      = os.urandom(32)
    rc4_key      = os.urandom(16)
    shuffle_seed = random.randint(0, 2**31)
    rolling_seed = random.randint(0, 2**31)

    raw = _xor_b(raw, xor_key)
    raw, indices = _shuffle(raw, shuffle_seed)
    raw = _rc4(raw, rc4_key)
    raw = _roll_xor(raw, rolling_seed)
    raw = base64.b64encode(raw)

    _step('Building output file with massive CJK junk code + hidden dynamic imports...')
    output = _build_output_file(
        do_hook, do_debug, do_vm, do_proxy, do_hide,
        repr(raw), xor_key, rc4_key, shuffle_seed, rolling_seed, indices,
        imp_fn_name=imp_fn_name
    )

    base_name = os.path.basename(path)
    out_path  = os.path.join(os.path.dirname(os.path.abspath(path)), 'obf-' + base_name)
    with open(out_path,'w',encoding='utf-8') as f: f.write(output)

    out_lines = output.count('\n')
    print()
    print(Colorate.Diagonal(Colors.DynamicMIX((Col.cyan,Col.blue)), f'>> Saved → {out_path}'))
    print(Colorate.Diagonal(_STYLE, f'>> Lines in output: {out_lines:,}'))
    print(Colorate.Diagonal(_STYLE, f'>> Payload: {len(raw):,} bytes'))
    flags = []
    if do_junk:  flags.append('AST-junk')
    if do_hide:  flags.append('hide-builtins')
    if do_debug: flags.append('anti-debug')
    if do_vm:    flags.append('anti-VM')
    if do_hook:  flags.append('anti-hook')
    if do_proxy: flags.append('anti-proxy')
    if flags: print(Colorate.Diagonal(_STYLE,'>> Features: '+'  |  '.join(flags)))

if __name__ == '__main__':
    main()
