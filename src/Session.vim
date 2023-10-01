let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Document/projects/sideProjects/inventoryMatcher/src
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +20 ~/Document/projects/sideProjects/inventoryMatcher/src/QuantityReconciliation/interactor/CreateAndApplyStrategyHandler.py
badd +121 ~/Document/projects/sideProjects/inventoryMatcher/src/main.py
badd +55 ~/Document/projects/sideProjects/inventoryMatcher/src/tasks.py
badd +30 ~/Document/projects/sideProjects/inventoryMatcher/src/QuantityReconciliation/infrastructure/repository/ReconciliationRepository.py
badd +20 QuantityReconciliation/Reconciler/entity/Reconciler.py
badd +21 QuantityReconciliation/infrastructure/projection/ReconcilerState.py
badd +7 QuantityReconciliation/infrastructure/eventStore/EventStore.py
badd +53 QuantityReconciliation/infrastructure/eventStore/EventStoreMongoDbImp.py
badd +6 ~/Document/projects/sideProjects/inventoryMatcher/src/QuantityReconciliation/Reconciler/domainEvent/ReconciliationWasInitialized.py
badd +1 ~/Document/projects/sideProjects/inventoryMatcher/src/QuantityReconciliation/Reconciler/domainEvent/ProblematicLineItemsInAmortizationTableExtracted.py
badd +11 ~/Document/projects/sideProjects/inventoryMatcher/src/QuantityReconciliation/interactor/InitializeReconciliationHandler.py
badd +2 ~/Document/projects/sideProjects/inventoryMatcher/src/QuantityReconciliation/infrastructure/command/CreateAndApplyStrategy.py
badd +1 ~/Document/projects/sideProjects/inventoryMatcher/src/shared/eventInfrastructure/DomainEvent.py
badd +87 ~/Document/projects/sideProjects/inventoryMatcher/src/QuantityReconciliation/infrastructure/eventStore/DomainEventDataMapper.py
badd +4 ~/Document/projects/sideProjects/inventoryMatcher/src/QuantityReconciliation/Reconciler/Strategy/domainEvents/StrategyWasChosen.py
argglobal
%argdel
$argadd .
edit QuantityReconciliation/Reconciler/entity/Reconciler.py
argglobal
balt QuantityReconciliation/infrastructure/projection/ReconcilerState.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 34 - ((24 * winheight(0) + 13) / 27)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 34
normal! 038|
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
