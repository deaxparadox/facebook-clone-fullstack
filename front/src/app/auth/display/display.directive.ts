import { Directive, ElementRef } from '@angular/core';


@Directive({
  selector: '[appDisplay]',
  standalone: true
})
export class DisplayDirective {

  constructor(private el: ElementRef) {
    this.el.nativeElement.style.height = `${screen.height}`;
    this.el.nativeElement.style.width = `${screen.width}`;
  }

}
