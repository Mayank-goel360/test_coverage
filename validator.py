import yaml

def get_nested(data: dict, path: str):
    """Safely walk a.b.c — return None if any step is missing."""
    cur = data
    for part in path.split('.'):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return cur

def exists(data: dict, path: str) -> bool:
    """True if get_nested(data, path) is not None."""
    return get_nested(data, path) is not None

def validate_context(data: dict, ctx_def: dict, errors: list, prefix="") -> bool:
    """
    Returns True if this context (+ subcontexts) pass; appends to errors if not.
    """
    flag = True
    name = ctx_def.get("name", "<unnamed>")
    ctx_id = f"[{prefix}{name}]"

    # Build the eval namespace
    ns = {
        "exists": lambda p: exists(data, p),
        "get":    lambda p: get_nested(data, p)
    }

    # 1) Check the 'when' clause
    when_expr = ctx_def.get("when", "True")
    try:
        if not eval(when_expr, {}, ns):
            return True  # this context does not apply
    except Exception as e:
        errors.append(f"{ctx_id} eval error `{when_expr}`: {e}")
        return False

    # 2) 'require' keys
    for key in ctx_def.get("require", []):
        if get_nested(data, key) is None:
            errors.append(f"{ctx_id} missing `{key}`")
            flag = False

    # 3) 'equals' assertions
    for key, expected in ctx_def.get("equals", {}).items():
        actual = get_nested(data, key)
        if actual is None:
            errors.append(f"{ctx_id} missing `{key}` for equals-check")
            flag = False
        elif actual != expected:
            errors.append(f"{ctx_id} `{key}` == {actual!r}, expected {expected!r}")
            flag = False

    # 4) Recurse into subcontexts
    for sub in ctx_def.get("subcontexts", []):
        if not validate_context(data, sub, errors, prefix + name + "/"):
            flag = False

    return flag

def validate_with_rules(data: dict, rules_path="/Users/mayankgoel/Desktop/Intern/endpoint/main/rules.yml"):
    """
    Returns (flag: bool, error_message: str)
    """
    with open(rules_path) as f:
        cfg = yaml.safe_load(f)

    errors = []
    flag = True

    for ctx in cfg.get("contexts", []):
        if not validate_context(data, ctx, errors):
            flag = False

    return flag, "\n".join(errors)
