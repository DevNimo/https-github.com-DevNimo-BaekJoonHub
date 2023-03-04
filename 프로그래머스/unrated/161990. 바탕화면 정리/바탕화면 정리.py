def solution(wallpaper):
    lx,ly,rx,ry = 50, -1 ,0,0
    for i,v in enumerate(wallpaper):
        if "#" in v:
            if ly == -1:
                ly = i
            ry = i+1
            r_index = len(v) - v[::-1].index("#")
            l_index = v.index("#")
            if lx >= l_index:
                lx = l_index
            if rx <= r_index:
                rx = r_index
            
        
    return [ly,lx,ry,rx]