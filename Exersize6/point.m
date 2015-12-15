function [x1, x2] = point( m0, m1, stdabw0, stdabw1 )
  p = 2*(m1*stdabw0^2-m0*stdabw1^2)/(stdabw1^2-stdabw0^2);
  q = (m0^2*stdabw1^2-m1^2*stdabw0^2 - 2*log(stdabw1/stdabw0)*stdabw0^2*stdabw1^2)/(stdabw1^2-stdabw0^2);
  x1 = (p/-2) + sqrt((p^2/4)-q);
  x2 = (p/-2) - sqrt((p^2/4)-q);
end

