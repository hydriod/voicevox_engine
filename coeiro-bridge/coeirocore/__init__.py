"""coeirocore 名義の橋渡しパッケージ。

エンジン（voicevox_engine fork）は `coeirocore.coeiro_manager` /
`coeirocore.query_manager` を import する。実体は coeirocore_rs なので、
サブモジュールを sys.modules へ別名登録して転送する。
"""

import sys as _sys

import coeirocore_rs.coeiro_manager as _coeiro_manager
import coeirocore_rs.model as _model
import coeirocore_rs.query_manager as _query_manager

_sys.modules[__name__ + ".coeiro_manager"] = _coeiro_manager
_sys.modules[__name__ + ".query_manager"] = _query_manager
_sys.modules[__name__ + ".model"] = _model

coeiro_manager = _coeiro_manager
query_manager = _query_manager
model = _model
