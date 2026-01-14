import { Keyboard } from "lucide-react"
import { IconButton } from "@/components/ui/button"
import { useToggle } from "@uidotdev/usehooks"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "./ui/dialog"
import useHotKey from "@/hooks/useHotkey"

interface ShortcutProps {
  content: string
  keys: string[]
}

function ShortCut(props: ShortcutProps) {
  const { content, keys } = props

  return (
    <div className="flex justify-between">
      <div>{content}</div>
      <div className="flex gap-[8px]">
        {keys.map((k) => (
          // TODO: 优化快捷键显示
          <div className="border px-2 py-1 rounded-lg" key={k}>
            {k}
          </div>
        ))}
      </div>
    </div>
  )
}

const isMac = function () {
  return /macintosh|mac os x/i.test(navigator.userAgent)
}

const CmdOrCtrl = () => {
  return isMac() ? "Cmd" : "Ctrl"
}

export function Shortcuts() {
  const [open, toggleOpen] = useToggle(false)

  useHotKey("h", () => {
    toggleOpen()
  })

  return (
    <Dialog open={open} onOpenChange={toggleOpen}>
      <DialogTrigger asChild>
        <IconButton tooltip="단축키">
          <Keyboard />
        </IconButton>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>단축키</DialogTitle>
          <div className="flex gap-2 flex-col pt-4">
            <ShortCut content="이동" keys={["Space + Drag"]} />
            <ShortCut content="확대/이동 초기화" keys={["Esc"]} />
            <ShortCut content="브러시 크기 감소" keys={["["]} />
            <ShortCut content="브러시 크기 증가" keys={["]"]} />
            <ShortCut content="원본 이미지 보기" keys={["Hold Tab"]} />

            <ShortCut content="실행 취소" keys={[CmdOrCtrl(), "Z"]} />
            <ShortCut content="다시 실행" keys={[CmdOrCtrl(), "Shift", "Z"]} />
            <ShortCut content="결과 복사" keys={[CmdOrCtrl(), "C"]} />
            <ShortCut content="이미지 붙여넣기" keys={[CmdOrCtrl(), "V"]} />
            <ShortCut
              content="수동 인페인팅 실행"
              keys={["Shift", "R"]}
            />
            <ShortCut content="단축키 창 전환" keys={["H"]} />
            <ShortCut content="설정 창 전환" keys={["S"]} />
            <ShortCut content="파일 관리자 전환" keys={["F"]} />
          </div>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  )
}

export default Shortcuts
