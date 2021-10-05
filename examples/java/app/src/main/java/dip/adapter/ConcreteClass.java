package dip.adapter;

import dip.domain.Interface;
import org.springframework.stereotype.Component;

@Component
public class ConcreteClass implements Interface {

    @Override
    public void method() {
        System.out.println("run ConcreteClass::method");
    }
}
