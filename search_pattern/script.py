def naive_pattern(text, pattern, **kwargs):
    replacement = kwargs.get('replacement', None)
    sensitive = kwargs.get('sensitive', False)
    cloned = ''
    num_skips = 0
    for text_idx in range(len(text)):
        if num_skips > 0:
            num_skips -= 1
            continue
        count = 0
        for p_idx in range(len(pattern)):
            if (sensitive and pattern[p_idx] == text[text_idx + p_idx]) or (
                    not sensitive and pattern[p_idx].lower() == text[text_idx + p_idx].lower()):
                count += 1
            else:
                break
        if count == len(pattern):
            print(f"{pattern} is found at index {text_idx}")
            if replacement is not None and len(pattern) != len(replacement):
                num_skips = len(pattern)
            if replacement is not None:
                cloned += replacement
        elif replacement is not None:
            cloned += text[text_idx]
    return cloned


naive_pattern('Hello World', 'o')
